#!/usr/bin/env python
# encoding: utf-8
from core.db.fields import *
from core.db.base_model import BaseModel


class Admin(BaseModel):
    """
    管理平台账户
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "admin"
        }
    }

    admin_id = IntField(primary_key=True)     # 账号ID
    login_name = StringField()     # 登陆账号
    password = StringField()     # 密码
    is_freeze = BooleanField()     # 状态
    role = StringField()     # 最高权限管理员:admin  普通管理员 member
