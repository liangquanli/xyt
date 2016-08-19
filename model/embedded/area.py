#!/usr/bin/env python
# encoding: utf-8
from core.db.base_model import EmbeddedModel
from core.db.fields import *


class Area(EmbeddedModel):

    province = StringField()     # 省
    city = StringField()     # 市