# !/usr/bin/env python
# encoding: utf-8
from flask import request, render_template, g
from xyt.model.foods import Food


def index():
    total, food_list = Food.searches({})
    return render_template(
        'xyt_index.html',
        food_list=food_list)


def member_center():
    return render_template(
        'member_center.html')


def order_list():
    return render_template(
        'orderlist.html')