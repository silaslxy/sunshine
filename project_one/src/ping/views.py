# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/7 11:08
# @Desc:
# ----------------------------------

from flask import Blueprint

from common.web.validate import http_validator
from ping.serializers import PingSerializer

bp = Blueprint("ping", __name__)


@bp.route("", methods=["GET"])
@http_validator(response_serializer=PingSerializer)
def index():
    res = PingSerializer()
    return res
