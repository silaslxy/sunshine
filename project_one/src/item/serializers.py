# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/6 16:47
# @Desc: 数据校验-viewObject和queryObject对象
# ----------------------------------

from datetime import datetime
from typing import List, Set
from uuid import UUID

from pydantic import BaseModel, Field, validator

from user.serializers import UserSerializer


class ItemSerializer(BaseModel):
    """
    项目数据序列化与校验
    """

    # example 可以列举一个值 做参考
    # default = ... 表示该字段必填
    # default = None 表示字段选填
    name: str = Field(default=..., description="姓名", max_length=15)
    description: str = Field(default=None, description="描述", max_length=15)
    tags: List[str] = Field(None, description="标签列表可选")
    require_tags: List[str] = Field(..., description="标签列表必填")
    unique_tags: Set[str] = Field(None, description="标签列表必填去重")
    user: UserSerializer = Field(None, description="用户信息")
    # max_items/min_items 设置列表的长度
    users: List[UserSerializer] = Field(..., description="用户信息列表", max_items=3, min_items=1)
    trace_id: UUID = Field(None, description="链路追踪id")
    create_time: datetime = Field(datetime.now(), description="创建时间")

    @validator("name", always=True)
    def validate_name(cls, value):
        """
        校验name字段
        :param value:
        :return:
        """
        if value == "test":
            raise ValueError("不能为test")
        return value

    # always=true无值的时候也验证
    # pre=true在标准验证器之前验证，标准验证器Filed带的验证等
    @validator("description", always=True)
    def validate_description(cls, value, values):
        """
        校验description字段, 需要限定一name字段的校验
        :param value:
        :param values:
        :return:
        """
        if "name" in values and value == values["name"]:
            raise ValueError("description的值不能和name一样")
        return value

    # 　可以定义预先检查的校验

    # class Config:
    #     validate_all = True

    # # 生成样本数据
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "xiaosiwen"
    #         }
    #     }
