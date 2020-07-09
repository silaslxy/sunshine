# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/9 10:25
# @Desc:
# ----------------------------------
from enum import Enum


class BaseCode(Enum):
    """
    自定义状态码返回
    """
    SUCCESS = 0, "请求成功"
    FAILURE = 600000001, "参数异常"
    SERVICE_ERROR = 600000002, "服务器异常"

    def code(self):
        return self.value[0]

    def msg(self):
        return self.value[1]
