#!/usr/bin/env python
# encoding: utf-8
import json
import copy
import datetime


class BaseField(object):
    """
    基础字段类
    """
    def __init__(self, **kwargs):
        super(BaseField, self).__init__()
        self._name = None
        self.default = kwargs.get('default')
        self.primary_key = kwargs.get('primary_key', False)

    def __get__(self, instance, owner):
        if not instance:
            raise Exception(u"不能从类调用对象属性")
        return instance._values.get(self._name, self.default)

    def __set__(self, instance, value):
        # if isinstance(instance, Serializer):     # 这里会循环引用
        # 如果初始化已完成而且该修改没在修改列表里面
        if self._name in instance._fields and self._name not in instance._change and instance._initialized:
            instance._change.append(self._name)
        instance._values[self._name] = value

    def loads(self, value):
        # 规定每一个field的loads都是传入字典数据传出对象中的数据格式
        return value

    def dumps(self, value):
        # 规定每一个field的dumps都是传入对象中的数据传出字典类型的值
        return value


class IntField(BaseField):
    def __init__(self, **kwargs):
        super(IntField, self).__init__(**kwargs)

    def loads(self, value):
        return int(value)

    def dumps(self, value):
        return int(value)


class FloatField(BaseField):
    def __init__(self, **kwargs):
        super(FloatField, self).__init__(**kwargs)

    def loads(self, value):
        return float(value)

    def dumps(self, value):
        return float(value)


class StringField(BaseField):
    def __init__(self, **kwargs):
        super(StringField, self).__init__(**kwargs)

    def loads(self, value):
        if isinstance(value, unicode):
            return value
        return value.decode('utf-8')

    def dumps(self, value):
        if isinstance(value, unicode):
            return value
        return value.encode('utf-8')


class JsonField(BaseField):
    def __init__(self, **kwargs):
        super(JsonField, self).__init__(**kwargs)

    def loads(self, value):
        return json.loads(value)

    def dumps(self, value):
        return json.dumps(value)


class TimeField(BaseField):
    def __init__(self, **kwargs):
        super(TimeField, self).__init__(**kwargs)

    def loads(self, value):
        return float(value)

    def dumps(self, value):
        return float(value)


class DateTimeField(BaseField):
    def __init__(self, **kwargs):
        super(DateTimeField, self).__init__(**kwargs)


class BooleanField(BaseField):
    def __init__(self, **kwargs):
        super(BooleanField, self).__init__(**kwargs)

    def loads(self, value):
        return bool(value)

    def dumps(self, value):
        return bool(value)


class ChangeAbleField(BaseField):
    """可变类型字段
    """
    def changed(self, instance, value):
        return True

    def __call__(self, *args, **kwargs):
        obj = self.__class__(*args, **kwargs)
        obj._name = self._name
        obj.default = self.default
        obj.primary_key = self.primary_key

        return obj


class ListField(ChangeAbleField):
    def __init__(self, field=None, **kwargs):
        super(ListField, self).__init__(**kwargs)
        self.field = field
        self._list = kwargs.get('default', list())

    def __get__(self, instance, owner):
        if not instance:
            raise Exception(u"不能从类调用对象属性")
        return instance._fields[self._name]._list     # 这里修改的事自己的数据保证父类是原始数据

    def __set__(self, instance, value):
        # 这里就是要求任何情况下这个家伙都在change列表里面就对了
        if self._name in instance._fields and self._name not in instance._change:     # and instance._initialized:
            instance._change.append(self._name)

        if not instance._initialized:     # 如果实例尚未初始化完毕
            instance._values[self._name] = value     # 实例赋值，保证实例的原始数据

        instance._fields[self._name]._list = value[:]     # 自身赋值

    def changed(self, instance, value):
        if value != instance._fields[self._name]._list:
            return True
        return False

    def loads(self, value):
        result_list = []
        for i in value:
            if not self.field:
                result_list.append(i)
            else:
                _i = self.field.loads(i)
                if _i:
                    result_list.append(self.field.loads(i))

        return result_list

    def dumps(self, value):
        result_list = []
        for i in self._list:
            if not self.field:
                result_list.append(i)
            else:
                _i = self.field.dumps(i)
                if _i:
                    result_list.append(self.field.dumps(i))

        return result_list

    def __call__(self, *args, **kwargs):
        obj = super(ListField, self).__call__(*args, **kwargs)
        obj._list = self._list

        return obj


class DictField(ChangeAbleField):
    def __init__(self, field=None, **kwargs):
        super(DictField, self).__init__(**kwargs)
        self.field = field
        self._dict = kwargs.get('default', dict())

    def __get__(self, instance, owner):
        if not instance:
            raise Exception(u"不能从类调用对象属性")
        return instance._fields[self._name]._dict     # 这里修改的事自己的数据保证父类是原始数据

    def __set__(self, instance, value):
        # 这里就是要求任何情况下这个家伙都在change列表里面就对了
        if self._name in instance._fields and self._name not in instance._change:     # and instance._initialized:
            instance._change.append(self._name)

        if not instance._initialized:     # 如果实例尚未初始化完毕
            instance._values[self._name] = value     # 实例赋值，保证实例的原始数据

        instance._fields[self._name]._dict = copy.deepcopy(value)     # 自身赋值

    def changed(self, instance, value):
        if value != instance._fields[self._name]._dict:
            return True
        return False

    def loads(self, value):
        result_dict = {}
        for i, v in value.iteritems():
            if not self.field:
                result_dict[i] = v
            else:
                result_dict[i] = self.field.loads(v)
        return result_dict

    def dumps(self, value):
        result_dict = {}

        for i, v in self._dict.iteritems():
            if not self.field:
                result_dict[i] = v
            else:
                result_dict[i] = v.dumps()
        return result_dict

    def __call__(self, *args, **kwargs):
        obj = super(DictField, self).__call__(*args, **kwargs)
        obj._dict = self._dict

        return obj


class EmbeddedModelField(BaseField):
    def __init__(self, base_document=None, *args, **kwargs):
        super(EmbeddedModelField, self).__init__(*args, **kwargs)

        self.embedded_model_type = base_document

    # def __get__(self, instance, owner):
    #     if not instance:
    #         raise Exception(u"不能从类调用对象属性")
    #
    #     _value_field = instance._values.get(self._name, self.default)
    #     if not _value_field:
    #         return None
    #     return _value_field.dumps()

    def __set__(self, instance, value):
        instance._change.append(self._name)
        instance._values[self._name] = value

    def loads(self, value):
        return self.embedded_model_type.loads(value)

    def dumps(self, value):
        if value:
            return value.dumps()
        else:
            return

    def changed(self, instance, value):
        if not value._change and value._initialized:     # 如果没变化而且初始化过了
            return False
        else:
            return True
