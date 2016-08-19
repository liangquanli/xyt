#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import BaseModel
from core.db.fields import *
from model.embedded.area import Area
from model.embedded.superior import Superior


class User(BaseModel):
    """
    用户信息
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "user"
        }
    }

    user_id = IntField(primary_key=True)
    user_name = StringField()     # 名字
    phone = StringField()     # 手机
    ID = StringField()     # 身份证号
    position = IntField()     # 职位
    partition_china = IntField()     # 所属大区
    area = ListField(field=EmbeddedModelField(base_document=Area))     # 行政区域
    email = StringField()     # 邮箱
    emergency_mobile = StringField()     # 紧急联系方式
    emergency_contact = StringField()     # 紧急联系人

    password = StringField()     # 密码
    superior = EmbeddedModelField(base_document=Superior)     # 上级管理
    is_freeze = BooleanField()     # 是否冻结

    creator_id = IntField()     # 创建者admin