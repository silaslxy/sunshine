# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/7 16:56
# @Desc:
# ----------------------------------
from pydantic import BaseModel, Field


class PageFilter(BaseModel):
    """
    分页参数
    """
    page_num: int = Field(default=1, description="当前页数", gt=1)
    page_size: int = Field(default=10, description="每页大小", gt=1, le=100)
