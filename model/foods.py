# !/usr/bin/env python
# encoding: utf-8
from core.db.base_model import BaseModel
from core.db.fields import *


class Food(BaseModel):
    _schema = {
        'mongo': {
            "database": "xyt",
            "collection": "foods"
        }
    }
    food_id = IntField(primary_key=True)
    name = StringField()    # '菜名'
    image = StringField()   # '展示图片'
    is_discount = BooleanField()    # '是否折扣'
    fixed_price = FloatField()      # '原价'
    discount_price = FloatField()   # '折扣价'
    order_count = IntField(default=0)       # '订单数'
