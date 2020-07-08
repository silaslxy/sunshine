# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/8 10:36 PM
# @Desc:
# ----------------------------------

import json
import logging
import os
import socket
import sys
from collections import OrderedDict

from flask import has_request_context, request

from common.util import datetime_helper


class JsonFormatter(logging.Formatter):
    """
    日志记录格式化，详细信息需要在考虑
    """

    def format(self, record: logging.LogRecord):
        super().format(record)
        s = record.getMessage()
        if record.exc_text:
            if s[-1:] != "\n":
                s = s + "\n"
            s = s + record.exc_text

        # 计算method_name
        cls_name = ''
        func_name = record.funcName
        count = 40
        f = sys._getframe()
        while f.f_code.co_name != func_name and count > 0:
            f = f.f_back
            count -= 1
        func_frame = f if f.f_code.co_name == func_name else None
        caller = func_frame.f_locals.get('self', None) if func_frame else None

        try:
            if caller:
                if not hasattr(caller, '__name__'):
                    caller = caller.__class__
                cls_name = '%s.%s' % (caller.__module__, caller.__name__)
        except:
            pass
        finally:
            method_name = '{cls_name}.{func_name}'.format(cls_name=cls_name, func_name=func_name)

        if has_request_context():
            url = request.url
            remote_addr = request.remote_addr
            host = request.host
        else:
            url = None
            remote_addr = None
            host = None

        msg = OrderedDict((
            ('@timestamp', datetime_helper.get_time_str()),
            ('level', record.levelname),
            ('project_name', os.environ.get('PROJECT_NAME', '')),
            ('project_version', os.environ.get('PROJECT_VERSION', '')),
            ("request_uri", getattr(record, 'request_uri', "")),
            ("trace_id", getattr(record, 'trace_id', "")),  # todo 通过thread获取trace_id?
            ("remote_ip", getattr(record, 'remote_ip', "")),
            ("user", getattr(record, 'user', "")),
            ("local_ip", socket.gethostbyname(socket.gethostname())),
            ("logger_name", record.name),
            ("method_name", method_name),
            ("line_number", record.lineno),
            ("thread_name", record.threadName),
            ("message", s),
            ("stack_trace", record.stack_info),
            ("url", url),
            ("remote_addr", remote_addr),
            ("host", host),
            ("message", s)
        ))
        return json.dumps(msg)


"""
通过配置文件配置
from logging.config import dictConfig
dictConfig({
    "version": 1,
    'loggers': {
        "": {
            "level": 'INFO',
            "handlers": ["default"],
            'propagate': False,
        }
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": "INFO",
        }
    },
    "formatters": {
        "json": {
            "class": "common.log.logger.JsonFormatter",
        }
    }

})
"""
