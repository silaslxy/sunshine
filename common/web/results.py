# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/8 9:39
# @Desc: 封装返回的数据格式
# ----------------------------------


from typing import TypeVar, Generic, Optional

from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class Success(GenericModel, Generic[DataT]):
    """
    成功响应
    """
    code: int = 0
    msg: str = "请求成功"
    data: Optional[DataT]


class Failure(GenericModel, Generic[DataT]):
    """
    失败响应
    """
    code: int
    msg: str
    data: Optional[DataT] = None


if __name__ == '__main__':
    Success[int](data=1)
