#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

import json
import urllib
import urllib2
try:
    from core.app import get_app
    logging = get_app().logger
except Exception, e:
    import logging


class SMSManager(object):
    """
    发送短消息
    """

    _instance = None

    @staticmethod
    def instance():
        assert hasattr(SMSManager, '_instance'), 'instance not initialized'
        return SMSManager._instance

    @staticmethod
    def set_instance(sms_mgr):
        """
        Sets a new instance for testing.
        :param sms_mgr:
        """

        SMSManager._instance = sms_mgr


class YunPianSMSManager(SMSManager):
    """
        使用云片网的API发送短信
    """

    def __init__(self):
        # self._api_key = secrets.get_secret('yunpian_api_key')  # 云片网分配的api key

        self._api_key = "811e4f9f9d2d4b6fc2eff853d54c08fb"
        self._sms_gateway_api_url = 'http://yunpian.com/v1/sms/send.json'  # 云片网普通调用接口地址
        self._sms_gateway_template_api_url = 'http://yunpian.com/v1/sms/tpl_send.json'  # 云片网模板调用接口地址

    def send_sms(self, description=None, **kwargs):
        """
        通过云片网的接口发送短信
        :param description:
        :param kwargs:
        """

        mobile = kwargs['mobile']

        gateway_api_url = None
        args = {
            'apikey': self._api_key,
            "mobile": mobile
        }
        if 'text' in kwargs:
            gateway_api_url = self._sms_gateway_api_url
            text = kwargs['text']  # 文字标识
            args.update({
                'text': text,
            })
        else:
            gateway_api_url = self._sms_gateway_template_api_url

            args.update({
                'tpl_id': kwargs['template_id'],
                'tpl_value': '&'.join(['#%s#=%s' % (k, v) for k, v in kwargs['template_value'].iteritems()])
            })

        args_str = urllib.urlencode(args)

        req = urllib2.Request(gateway_api_url, args_str)
        response = urllib2.urlopen(req, timeout=3)
        response_str = response.read()

        if response.getcode() != 200:
            raise Exception(
                'Yun Pian API error: %d %r [%s] (args: %r)' % (response.getcode(), response.msg, response_str, args_str))

        logging.info('sent sms to: %s, description: %s, args: %s' % (mobile, description or '', args_str))
        return json.loads(response_str)
