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
    # 第1,2位代表项目组（数据中台66） 第3,4位代表项目（通用00） 第5,6位代表模块（通用00） 第7,8位代表模块内异常
    # 如数据中台 反欺诈项目（01） 态势感知（01） 模块A-----66010101 可以添加位数定义更详细的异常
    SUCCESS = 0, "请求成功"
    PARAM_ERROR = 66000001, "参数异常"
    SERVICE_ERROR = 66000002, "服务器异常"

    def code(self):
        return self.value[0]

    def msg(self):
        return self.value[1]
