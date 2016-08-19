#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import BaseModel
from core.db.fields import *


class PartitionChina(BaseModel):
    """
    大区
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "partition_china"
        }
    }

    partition_id = IntField(primary_key=True)
    name = StringField()
    is_freeze = BooleanField()
