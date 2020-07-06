# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:44
# @Desc: 接口
# ----------------------------------


from flask import Blueprint

bp = Blueprint("model_a", __name__)


@bp.route("", methods=["GET"])
def index():
    return "hello world"
