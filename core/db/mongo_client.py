#!/usr/bin/env python
# encoding: utf-8
from pymongo import MongoClient
from core import settings


_mongo_clients = None


def get_mongo_client():
    """
    获取mongo客户端
    :param name:
    :return:
    """
    global _mongo_clients

    if not _mongo_clients:
        _mongo_config = settings.mongo_settings

        _mongo_clients = MongoClient(
            host=_mongo_config['host'],
            port=_mongo_config['port'],
            use_greenlets=_mongo_config['use_greenlets']
        )

    return _mongo_clients


def clear():
    global _mongo_clients

    _mongo_clients = None