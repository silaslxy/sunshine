# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:44
# @Desc: 接口
# ----------------------------------

from flask import Blueprint, request

from common.web import http_validator
from user.enums import UserCategoryEnum
from user.serializers import CategoryDetailSerializer, UserSerializer

bp = Blueprint("user", __name__)


@bp.route("", methods=["POST"])
@http_validator(body_serializer=UserSerializer, response_serializer=UserSerializer)
def create_user():
    """
    创建用户
    :return:
    """
    return request.body


@bp.route("/<category>", methods=["GET"])
@http_validator(response_serializer=CategoryDetailSerializer)
def get_category_detail(category: str):
    """
    根据类型获取介绍
    :param category:
    :return:
    """
    res = CategoryDetailSerializer()
    res.category = category
    if category == UserCategoryEnum.student:
        res.description = "学生"
    else:
        res.description = "老师"
    return res
