#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

from oss import oss_api

from core import settings


class AliOSSClient(object):
    """
    ali oss client
    """

    _oss_settings = {}

    def __init__(self, cfg):
        self._current = oss_api.OssAPI(**cfg)

    def __getattr__(self, name):
        return getattr(self._current, name)

    @staticmethod
    def instance(name="default"):
        """
        实例化
        """
        cfg = settings.oss_settings.get(name)
        if not cfg:
            raise ValueError("未设置名字为%s的oss_settings配置信息" % name)
        return AliOSSClient(cfg)


def get_oss_client(name):
    return AliOSSClient.instance(name)
