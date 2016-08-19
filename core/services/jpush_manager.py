#!/usr/bin/env python
# encoding: utf-8
from core import settings
import jpush


def jpush_notification_to_app(app_key, alert, extra, apns_production=False):
    """
    通过极光广播提醒到全部设备
    :param app_key: 育儿平台应用 key
    :param alert: 通知内容
    :param extra: 供业务使用的字典
    :param apns_production: True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。
    :return:
    """
    jpush_settings = settings.jpush_settings[app_key]
    _jpush = jpush.JPush(jpush_settings["appkey"], jpush_settings["mastersecret"])

    push = _jpush.create_push()
    push.audience = jpush.all_  # 广播提醒到全部设备
    ios_msg = jpush.ios(alert=alert, badge="+1", extras=extra)
    android_msg = jpush.android(alert=alert, extras=extra)
    push.notification = jpush.notification(alert=alert, android=android_msg, ios=ios_msg)
    push.options = {"apns_production": apns_production}
    #push.options = {"apns_production": jpush_settings["apns_production"]}
    push.platform = jpush.all_
    try:
        print push.send()
    except Exception, e:
        if e.error_code == 1011:
            pass
        else:
            raise e


def jpush_notification_to_tags(app_key, tags, alert, extra, apns_production=False):
    """
    通过极光发送通知到基于标签的用户群
    :param app_key:
    :param tags:
    :param alert: 通知内容
    :param extra: 供业务使用的字典
    :param apns_production: True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。
    :return:
    """
    jpush_settings = settings.jpush_settings[app_key]
    _jpush = jpush.JPush(jpush_settings["appkey"], jpush_settings["mastersecret"])

    push = _jpush.create_push()
    push.audience = jpush.audience(jpush.tag(*tags))
    ios_msg = jpush.ios(alert=alert, badge="+1", extras=extra)
    android_msg = jpush.android(alert=alert, extras=extra)
    push.notification = jpush.notification(alert=alert, android=android_msg, ios=ios_msg)
    push.options = {"apns_production": apns_production}
    #push.options = {"apns_production": jpush_settings["apns_production"]}
    push.platform = jpush.all_
    try:
        print push.send()
    except Exception, e:
        if e.error_code == 1011:
            pass
        else:
            raise e


def jpush_notification_to_alias(app_key, alias, alert, extra, apns_production=False):
    """
    通过极光发送通知到别名用户设备
    :param app_key:
    :param alias:
    :param alert: 通知内容
    :param extra: 供业务使用的字典
    :param apns_production: True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。
    :return:
    """
    jpush_settings = settings.jpush_settings[app_key]
    _jpush = jpush.JPush(jpush_settings["appkey"], jpush_settings["mastersecret"])

    push = _jpush.create_push()
    push.audience = jpush.audience(jpush.alias(*alias))
    ios_msg = jpush.ios(alert=alert, badge="+1", extras=extra)
    android_msg = jpush.android(alert=alert, extras=extra)
    push.notification = jpush.notification(alert=alert, android=android_msg, ios=ios_msg)
    push.options = {"apns_production": apns_production}
    #push.options = {"apns_production": jpush_settings["apns_production"]}
    push.platform = jpush.all_
    #print push.payload
    try:
        print push.send()
    except Exception, e:
        if e.error_code == 1011:
            pass
        else:
            raise e

def jpush_notification_to_registration_ids(app_key, reg_ids, alert, extra, apns_production=False):
    """
    通过极光发送通知到指定极光分配的 注册号的用户设备
    :param app_key:
    :param reg_ids:
    :param alert: 通知内容
    :param extra:
    :param apns_production: True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。
    :return:
    """
    jpush_settings = settings.jpush_settings[app_key]
    _jpush = jpush.JPush(jpush_settings["appkey"], jpush_settings["mastersecret"])

    push = _jpush.create_push()
    push.audience = jpush.audience(jpush.registration_id(*reg_ids))
    ios_msg = jpush.ios(alert=alert, badge="+1", extras=extra)
    android_msg = jpush.android(alert=alert, extras=extra)
    push.notification = jpush.notification(alert=alert, android=android_msg, ios=ios_msg)
    push.options = {"apns_production": apns_production}
    #push.options = {"apns_production": jpush_settings["apns_production"]}
    push.platform = jpush.all_
    try:
        print push.send()
    except Exception, e:
        if e.error_code == 1011:
            pass
        else:
            raise e


#push message
def jpush_message_to_app(app_key, msg_content, extra, apns_production=False):
    """
    通过极光发送自定义消息到应用
    :param app_key:
    :param msg_content:
    :param extra:
    :param apns_production: True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。
    :return:
    """
    jpush_settings = settings.jpush_settings[app_key]
    _jpush = jpush.JPush(jpush_settings["appkey"], jpush_settings["mastersecret"])

    push = _jpush.create_push()
    push.audience = jpush.all_
    push.message = jpush.message(msg_content=msg_content, extras=extra)
    push.options = {"apns_production": apns_production}
    #push.options = {"apns_production": jpush_settings["apns_production"]}
    push.platform = jpush.all_
    try:
        print push.send()
    except Exception, e:
        if e.error_code == 1011:
            pass
        else:
            raise e


def jpush_message_to_tags(app_key, tags, msg_content, extra_data, apns_production=False):
    """
    通过极光发送自定义消息到标签用户
    :param app_key:
    :param tags:
    :param msg_content:
    :param extra_data:
    :param apns_production: True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。
    :return:
    """
    jpush_settings = settings.jpush_settings[app_key]
    _jpush = jpush.JPush(jpush_settings["appkey"], jpush_settings["mastersecret"])

    push = _jpush.create_push()
    push.audience = jpush.audience(jpush.tag(*tags))
    push.message = jpush.message(msg_content=msg_content, extras=extra_data)
    push.options = {"apns_production": apns_production}
    #push.options = {"apns_production": jpush_settings["apns_production"]}
    push.platform = jpush.all_
    try:
        print push.send()
    except Exception, e:
        if e.error_code == 1011:
            pass
        else:
            raise e


def jpush_message_to_alias(app_key, alias, msg_content, extra_data, apns_production=False):
    """
    通过极光发送自定义消息到别名用户
    :param app_key:
    :param alias:
    :param msg_content:
    :param extra_data:
    :param apns_production: True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。
    :return:
    """
    jpush_settings = settings.jpush_settings[app_key]
    _jpush = jpush.JPush(jpush_settings["appkey"], jpush_settings["mastersecret"])

    push = _jpush.create_push()
    push.audience = jpush.audience(jpush.alias(*alias))
    push.message = jpush.message(msg_content=msg_content, extras=extra_data)
    push.options = {"apns_production": apns_production}
    #push.options = {"apns_production": jpush_settings["apns_production"]}
    push.platform = jpush.all_
    try:
        print push.send()
    except Exception, e:
        if e.error_code == 1011:
            pass
        else:
            raise e

def jpush_message_to_registration_ids(app_key, reg_ids, msg_content, extra_data, apns_production=False):
    """
    通过极光发送自定义消息到激光注册标识的设备
    :param app_key:
    :param reg_ids:
    :param msg_content:
    :param extra_data:
    :param apns_production: True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。
    :return:
    """
    jpush_settings = settings.jpush_settings[app_key]
    _jpush = jpush.JPush(jpush_settings["appkey"], jpush_settings["mastersecret"])

    push = _jpush.create_push()
    push.audience = jpush.audience(jpush.registration_id(*reg_ids))
    push.message = jpush.message(msg_content=msg_content, extras=extra_data)
    push.options = {"apns_production": apns_production}
    #push.options = {"apns_production": jpush_settings["apns_production"]}
    push.platform = jpush.all_
    try:
        print push.send()
    except Exception, e:
        if e.error_code == 1011:
            pass
        else:
            raise e


