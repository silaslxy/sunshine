# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:44
# @Desc: 接口层-调用service层
# ----------------------------------


from flask import Blueprint, request
from flask_pydantic import validate

from item.filters import ItemFilter
from item.serializers import ItemSerializer

bp = Blueprint("item", __name__)


@bp.route("", methods=["POST"])
@validate(body=ItemSerializer)
def create_item():
    """
    创建项目详细介绍
    :return:
    """
    return request.body_params


@bp.route("/<item_id>", methods=["GET"])
@validate(query=ItemFilter)
def get_item_by_id(item_id: int):
    """
    根据id获取项目详情
    :param item_id:
    :return:
    """
    return request.query_params
