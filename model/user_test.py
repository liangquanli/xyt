#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import BaseModel, EmbeddedModel
from core.db.fields import *


class AddressTest(EmbeddedModel):

    area = StringField()
    address = StringField()
    fuck = DictField()
    fuck2 = ListField(field=StringField())


class UserTest(BaseModel):
    """
    用户数据
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "user_test"
        }
    }

    user_id = IntField(primary_key=True)
    user_name = StringField()
    user_test1 = ListField(field=IntField())
    user_test2 = DictField()
    user_test3 = EmbeddedModelField(base_document=AddressTest)
    user_test4 = ListField(field=EmbeddedModelField(base_document=AddressTest))

    user_date = DateTimeField()