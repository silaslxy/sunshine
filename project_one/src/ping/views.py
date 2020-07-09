# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/7 11:08
# @Desc:
# ----------------------------------

import logging

from flask import Blueprint

from common.web import http_validator
from ping.serializers import PingSerializer

bp = Blueprint("ping", __name__)

logger = logging.getLogger(__name__)


@bp.route("", methods=["GET"])
@http_validator(response_serializer=PingSerializer)
def ping():
    """
    检测服务接口
    :return:
    """
    res = PingSerializer()
    logger.error("aaaaaaa")
    logger.info("aaaaaaa")
    logger.warning("aaaaaaa")
    logger.debug("aaaa")
    return res
