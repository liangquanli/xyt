#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import BaseModel
from core.db.fields import *


class City(BaseModel):
    """
    市
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "city"
        }
    }

    name = StringField(primary_key=True)
    short_name = StringField()
    parent_name = StringField()
    position_x = FloatField()
    position_y = FloatField()
