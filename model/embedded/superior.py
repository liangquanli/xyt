#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import EmbeddedModel
from core.db.fields import *


class Superior(EmbeddedModel):

    general_id = IntField()     # 总经理ID
    partition_china_id = IntField()     # 大区经理
    province_id = IntField()     # 省经理