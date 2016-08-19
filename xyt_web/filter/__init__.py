#!/usr/bin/env python
# encoding: utf-8
from core.app import app
from finance_web.filter import time_monitor


global_pre_handler = []
global_post_handler = []


@app.before_request
def before(**kwargs):
    for i in global_pre_handler:
        i()


@app.after_request
def after(response, **kwargs):
    for i in global_post_handler:
        i()

    return response