#!/usr/bin/env python
# encoding: utf-8
host = '0.0.0.0'

port = 10050
debug = True

secret_key = '4\xe2y\xd9\x80\xb6\x854@\xef\x1a\x16^&\xd9\xdc\xd8G\xd0\x90\xe0\xe6\x07u'

SENTRY_DSN = 'http://9db88f4936f744d89937cd9fc6d41b8d:4e638550e3c344cc92274b6a71c4f45d@sentry.ykdllmyr.com/66'

mongo_settings = {
    # 'host': "mongodb://ykdl:bf616d8ef6e2e9d59c7e94e25f35897f@121.42.146.230",
    'host': "mongodb://10.251.24.57",
    'port': 27017,
    'use_greenlets': True
}

memcached_settings = {
    # "servers": ["121.42.146.230:11211"]
    "servers": ["127.0.0.1:11211"]
    # "servers": "ad8678fc4ac3452c.m.cnqdalicm9pub001.ocs.aliyuncs.com:11211",
    # "username": "ad8678fc4ac3452c",
    # "password": "dewE12Ck9Z0oXckp12",
}