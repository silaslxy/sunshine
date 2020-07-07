# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/7 11:08
# @Desc:
# ----------------------------------

from flask import Blueprint
from flask_pydantic import validate

from ping.serializers import PingSerializer

bp = Blueprint("ping", __name__)


@bp.route("", methods=["GET"])
def index():
    res = PingSerializer()
    return res.dict()