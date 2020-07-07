# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/7 11:10
# @Desc:
# ----------------------------------

from pydantic import BaseModel, Field


class PingSerializer(BaseModel):
    """
    接口返回的序列化
    """

    # default:设置默认值
    # description: 字段描述
    # max_length: 字符长度限制
    pong: str = Field(default="pong", description="ping-pong", max_length=15)
