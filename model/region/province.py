#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import BaseModel
from core.db.fields import *


class Province(BaseModel):
    """
    省
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "province"
        }
    }

    name = StringField(primary_key=True)
    short_name = StringField()
    partition_id = IntField()     # 所属大区编号,无大区为0
