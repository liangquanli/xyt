#!/usr/bin/env python
# encoding: utf-8
import bmemcached
from core import settings


_memcached_clients = None


def get_memcached_client():
    """
    获取memcacehd客户端
    :return:
    """
    global _memcached_clients

    if not _memcached_clients:
        _memcached_config = settings.memcached_settings

        _memcached_clients = bmemcached.Client(**_memcached_config)

    return _memcached_clients


def clear():
    global _memcached_clients

    _memcached_clients = None