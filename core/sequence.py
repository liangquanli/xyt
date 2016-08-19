#!/usr/bin/env python
# encoding: utf-8
from core.db.mongo_client import get_mongo_client


def generate_sequence(name):
    """
    生成顺序号
    :param name:
    :return:
    """
    mongo = get_mongo_client()

    # 连接育儿平台基础库
    re = mongo.sales_tools.sequences.find_and_modify(
        query={"name": name},
        update={"$inc": {"sequence": 1}},
        upsert=True,
        new=True)

    return int(re["sequence"])
