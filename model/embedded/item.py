#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import EmbeddedModel
from core.db.fields import *


class Item(EmbeddedModel):
    product_id = IntField()
    product_discount = FloatField()
    amount = IntField()
    product_name = StringField()
    product_price = IntField()
    warehouseex_number = IntField()

