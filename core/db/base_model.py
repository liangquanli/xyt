#!/usr/bin/env python
# encoding: utf-8
import copy
from fields import BaseField, ChangeAbleField, EmbeddedModelField
from core.db.mongo_client import get_mongo_client


class SerializerMetaClass(type):
    """
    序列化类的元类
    """

    def __init__(cls, name, bases, attrs):
        super(SerializerMetaClass, cls).__init__(name, bases, attrs)

        cls._field_for_class = {}

        for attr_name, attr_value in attrs.iteritems():
            if isinstance(attr_value, BaseField):
                cls._field_for_class[attr_name] = attr_value

                attr_value._name = attr_name  # 反向管理把属性名记录到属性自身

                if attr_value.primary_key:
                    cls.primary_key = attr_name

        father = bases[0]
        if isinstance(father, SerializerMetaClass):
            cls._field_for_class.update(father._field_for_class)

        # 主键从父类继承下来(如果父类有主键的话)
        if hasattr(father, 'primary_key') and father.primary_key:
            cls.primary_key = father.primary_key


class Serializer(object):
    """
    可以序列化的类
    """
    __metaclass__ = SerializerMetaClass

    def __init__(self):
        super(Serializer, self).__init__()
        self._change = []
        self._initialized = False
        self._values = {}
        self._fields = {}

        for attr_name, field in self._field_for_class.iteritems():
            self._values[attr_name] = field.default
            if callable(field):
                self._fields[attr_name] = copy.deepcopy(field)
                self._change.append(attr_name)
            else:
                self._fields[attr_name] = field

    @classmethod
    def loads(cls, data):
        """
        从一个字典对象还原出属性
        :param data: 字典数据
        :return: obj 对象
        """
        obj = cls()
        for attr_name, attr_obj in obj._fields.iteritems():
            # 这里调用每一个field的loads,规定每一个field的loads都是传入字典数据传出对象中的数据格式，然后在此赋值
            if attr_name not in data:
                continue
            field_data = attr_obj.loads(data[attr_name])
            setattr(obj, attr_name, field_data)

        obj._initialized = True  # 设置初始化已完成
        return obj

    def dumps(self):
        """
        把自身这个对象还原成字典
        :return: dict 字典对象
        """
        data = {}
        for attr_name, value in self._values.iteritems():
            # _id就不打印出来了
            if attr_name == '_id':
                continue

            if value is None:
                continue

            # 这里调用每一个field的dumps，规定每一个field的dumps都是传入对象中的数据传出字典类型的值，然后在此拼装
            attr_obj = self._fields[attr_name]
            data[attr_name] = attr_obj.dumps(value)

        return data

    def dump_changes(self):
        data = {}

        for attr_name in self._change:
            value = self._values[attr_name]
            attr_obj = self._fields[attr_name]

            if isinstance(attr_obj, (ChangeAbleField, EmbeddedModelField)):
                if attr_obj.changed(self, value):
                    data[attr_name] = attr_obj.dumps(value)
            else:
                data[attr_name] = value

        return data


class BaseModel(Serializer):

    _id = BaseField()
    primary_key = None

    _schema = {}

    def __init__(self):
        super(BaseModel, self).__init__()

    @classmethod
    def get_mongo_collection(cls):
        return get_mongo_client()[cls._schema['mongo']['database']][cls._schema['mongo']['collection']]

    @classmethod
    def get(cls, pk_id):
        col = cls.get_mongo_collection()
        if not cls.primary_key:
            raise ValueError("%s类没有主键" % cls.__name__)

        data = col.find_one({cls.primary_key: pk_id})
        if not data:
            return None

        obj = cls.loads(data)
        return obj

    @classmethod
    def search(cls, query_dict):
        col = cls.get_mongo_collection()
        data = col.find_one(query_dict)

        if not data:
            return None

        obj = cls.loads(data)
        return obj

    @classmethod
    def searches(cls, query_dict, sort=None, offset=0, limit=0, count_total=False):
        """

        :param query_dict: 搜索条件
        :param sort: 排序条件 [
                    ('field1', pymongo.ASCENDING),
                    ('field2', pymongo.DESCENDING)]
        :param offset: 数据起始游标
        :param limit: 数量
        :param count_total: 是否统计总数
        :return:
        """
        col = cls.get_mongo_collection()
        cur = col.find(query_dict)

        if sort:
            cur = cur.sort(sort)
        if offset:
            cur = cur.skip(offset)
        if limit:
            cur = cur.limit(limit)

        objs = []
        for i in cur:
            obj = cls.loads(i)
            objs.append(obj)

        total = None
        if count_total:
            total = cur.count()

        return total, objs

    def save(self):
        col = self.get_mongo_collection()

        if self._initialized:     # 如果已经初始化
            data = self.dump_changes()
            if data:
                col.update({'_id': self._id}, {'$set': data})
        else:
            data = self.dumps()
            _id = col.save(data)

            self._initialized = True

        return self

    def create(self):
        col = self.get_mongo_collection()

        data = self.dumps()
        _id = col.save(data)

        new_obj = self.loads(data)
        new_obj._values['_id'] = _id

        return new_obj

    @classmethod
    def creates(cls, data_list):
        col = cls.get_mongo_collection()

        obj_ids = col.insert_many(data_list)
        return obj_ids

    def update(self, query_dict, data, multi=False):
        col = self.get_mongo_collection()
        col.update(query_dict, {'$set': data}, multi=multi)
        return self


class EmbeddedModel(Serializer):

    def __init__(self):
        super(EmbeddedModel, self).__init__()