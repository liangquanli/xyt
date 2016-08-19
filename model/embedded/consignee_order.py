#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import EmbeddedModel
from core.db.fields import *
from model.embedded.area import Area


class ConsigneeOrder(EmbeddedModel):
    name = StringField()  # 收货人姓名
    phone = StringField()  # 收货人电话

    area = EmbeddedModelField(base_document=Area)
    address = StringField()  # 地址

    ds_id = IntField()  # 关联药店id
