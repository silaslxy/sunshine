# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:35
# @Desc:
# ----------------------------------
import logging

from common.log.logger import JsonFormatter

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(JsonFormatter())
stream_handler.setLevel(logging.DEBUG)
