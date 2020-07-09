# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/9 9:31
# @Desc: 设置app的一些默认属性
# ----------------------------------
import json
import logging

from flask import Flask

from common.log import stream_handler
from common.web import BaseCode


def default_app(app: Flask):
    """
    设置app的日志格式
    设置app返回数据
    设置app其他中间件
    :param app:
    :return:
    """
    # 设置日志
    if not app.debug:
        app.logger.root.addHandler(stream_handler)
        app.logger.root.setLevel(logging.INFO)

    # 处理返回数据
    @app.after_request
    def render(response):
        # 成功响应
        if response.status_code == 200:
            if response.content_type == "application/json":
                response.data = json.dumps({
                    "code": BaseCode.SUCCESS.code(),
                    "msg": BaseCode.SUCCESS.msg(),
                    "data": response.json
                })
        elif 400 <= response.status_code < 500:
            if response.content_type == "application/json":
                response.data = json.dumps({
                    "code": BaseCode.PARAM_ERROR.code(),
                    "msg": BaseCode.PARAM_ERROR.msg(),
                    "data": None
                })
                response.status_code = 200
        else:
            if response.content_type == "application/json":
                response.data = json.dumps({
                    "code": response.status_code,
                    "msg": BaseCode.SERVICE_ERROR.msg(),
                    "data": None
                })
                response.status_code = 200

        return response
