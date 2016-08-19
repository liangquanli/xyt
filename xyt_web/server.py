#!/usr/bin/env python
# encoding: utf-8
import os
import sys
from gevent.wsgi import WSGIServer
from raven.contrib.flask import Sentry

reload(sys)
sys.setdefaultencoding('utf8')
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cur_dir, "../"))
sys.path.insert(0, os.path.join(cur_dir, "../../"))

env = 'debug'
if __name__ == '__main__':
    from core import settings
    from core.app import init_app

    app = init_app(__name__)
    if len(sys.argv) > 1:
        env = sys.argv[1]

    from core.services import sms_mgr
    from xyt_web.urls import setup_filter, init_url

    sms_mgr.SMSManager.set_instance(sms_mgr.YunPianSMSManager())
    settings.import_from_path('xyt_web.conf.%s' % env)
    setup_filter()
    init_url(app)
    sentry = Sentry(dsn=settings.SENTRY_DSN)
    sentry.init_app(app)
    app.debug = True
    app.secret_key = settings.secret_key

    http_server = WSGIServer((settings.host, settings.port), app)
    http_server.serve_forever()
