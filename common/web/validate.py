# coding: utf-8
# ----------------------------------
# @Author: xiaosiwen
# @Date: 2020/7/8 16:05
# @Desc:
# ----------------------------------


import json
from functools import wraps
from typing import Optional, TypeVar

from flask import request, make_response
from pydantic import ValidationError

BODY_SERIALIZER = TypeVar("BODY_SERIALIZER")
QUERY_SERIALIZER = TypeVar("QUERY_SERIALIZER")
RESPONSE_SERIALIZER = TypeVar("RESPONSE_SERIALIZER")


def http_validator(body_serializer: Optional[BODY_SERIALIZER] = None,
                   query_serializer: Optional[QUERY_SERIALIZER] = None,
                   response_serializer: Optional[RESPONSE_SERIALIZER] = None
                   ):
    """
    请求body，query, response的校验
    :param body_serializer:
    :param query_serializer:
    :param response_serializer:
    :return:
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if body_serializer:
                try:
                    # add body obj to request
                    request.body = body_serializer(**request.json)
                except ValidationError as e:
                    return make_response({"validation_error": e.errors()}, 400)

            if query_serializer:
                try:
                    # field type is array
                    is_array_field = []
                    for field, filed_attr in query_serializer.schema().get("properties", {}).items():
                        if filed_attr.get("type") == "array":
                            is_array_field.append(field)

                    # query string to query dict
                    query_dict = {}
                    for query_item in request.query_string.decode().split("&"):
                        cur = query_item.split("=")
                        if len(cur) != 2:
                            continue
                        field_name = cur[0]
                        field_value = cur[1]
                        if field_name in is_array_field:
                            if field_name in query_dict:
                                query_dict[field_name].append(field_value)
                            else:
                                query_dict[field_name] = [field_value]
                        else:
                            query_dict[field_name] = field_value
                    # add query obj to request
                    request.query = query_serializer(**query_dict)

                except ValidationError as e:
                    return make_response({"validation_error": e.errors()}, 400)

            res = func(*args, **kwargs)

            if response_serializer:
                if not isinstance(res, response_serializer):
                    return make_response({"response_error": [{"loc": None,
                                                              "msg": "return type is not %s" % response_serializer,
                                                              "type": "response_error"}]}, 400)
                return make_response(json.loads(res.json()), 200)

            return res

        return wrapper

    return decorator
