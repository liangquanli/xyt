#!/usr/bin/env python
# encoding: utf-8
from flask import Flask


app = None


def init_app(name):
    global app
    app = Flask(name)
    return app


def get_app():
    return app