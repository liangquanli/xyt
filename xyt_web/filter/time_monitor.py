#!/usr/bin/env python
# encoding: utf-8
import time
from flask import g
from core.app import app


def time_start():
    g.time_start = time.time()


def time_end():
    time_view = time.time() - g.time_start
    app.logger.info('time_view: %s' % time_view)