# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:44
# @Desc: 接口层-调用service层
# ----------------------------------
import logging

from flask import Blueprint, request

from common.web import http_validator
from item.filters import ItemFilter
from item.serializers import ItemSerializer

bp = Blueprint("item", __name__)

logger = logging.getLogger(__name__)


@bp.route("", methods=["POST"])
@http_validator(body_serializer=ItemSerializer, response_serializer=ItemSerializer)
def create_item():
    """
    创建项目详细介绍
    :return:
    """
    logger.info("aaaaaaa")
    return request.body


@bp.route("/<item_id>", methods=["GET"])
@http_validator(query_serializer=ItemFilter, response_serializer=ItemFilter)
def get_item_by_id(item_id: int):
    """
    根据id获取项目详情
    :param item_id:
    :return:
    """
    return request.query
