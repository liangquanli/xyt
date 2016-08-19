#!/usr/bin/env python
# encoding: utf-8
from flask.views import MethodView, MethodViewType
from xyt_web.views import index


def setup_filter():
    pass


def init_url(app):
    """
    初始化url
    :param app: Flask进程
    :return:
    """
    def url(url_rule, view, endpoint=None, **options):
        if type(view) is MethodViewType and issubclass(view, MethodView):
            view = view.as_view(str(endpoint))
        app.add_url_rule(url_rule, endpoint=endpoint, view_func=view, **options)

    url("/", index.index)

    url("/member_center", index.member_center)

    url("/order_list", index.order_list)
