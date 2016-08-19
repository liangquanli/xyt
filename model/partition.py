#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import BaseModel
from core.db.fields import *


class Partition(BaseModel):
    """
    大区信息
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "partition_china"
        }
    }

    partition_id = IntField(primary_key=True)    # 大区id
    name = StringField()     # 名字
