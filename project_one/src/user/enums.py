# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/7 11:32
# @Desc:
# ----------------------------------

from enum import Enum


class UserCategoryEnum(str, Enum):
    """
    用户类型枚举
    """
    student = "STUDENT"
    teacher = "TEACHER"

