# !/usr/bin/env python
# encoding: utf-8
from flask import request, render_template, g


def index():
    return render_template(
        'xyt_index.html')


def member_center():
    return render_template(
        'member_center.html')


def order_list():
    return render_template(
        'orderlist.html')