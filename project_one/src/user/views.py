# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:44
# @Desc: 接口
# ----------------------------------

from flask import Blueprint, request
from user.enums import UserCategoryEnum
from user.serializers import CategoryDetailSerializer, UserSerializer
from user.filters import PageFilter

bp = Blueprint("user", __name__)


@bp.route("", methods=["POST"])
def create_user():
    """
    创建用户
    :param user_serializer:
    :return:
    """

    body = request.body_params
    return body


@bp.route("/<category>", methods=["GET"])
# @validate(query=PageFilter)
def get_category_detail(category: str):
    """
    根据类型获取介绍
    :param category:
    :return:
    """
    # query = request.query_params
    res = CategoryDetailSerializer()
    res.category = category
    if category == UserCategoryEnum.student:
        res.description = "学生"
    else:
        res.description = "老师"
    # 只能返回json
    return res.json()
