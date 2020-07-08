# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/7 16:56
# @Desc:
# ----------------------------------
from typing import List

from pydantic import BaseModel, Field


class ItemFilter(BaseModel):
    name: str = Field(..., max_length=50, description="名称")
    names: List[str] = Field(None, description="名称批量查询", max_items=2)