# coding:UTF-8
"""
公共装饰器
@author: YYJ
创建于2019年10月5日
"""

from traceback import format_tb
from functools import wraps
from flask import request, Response
import json


def catch_error(func):
    @wraps(func)
    def _handle(*k, **v):
        try:
            return func(*k, **v)
        except Exception as error:
            print(format_tb(error.__traceback__), type(error), error)
            resp = Response(json.dumps({"code": 404, "error": error}))
            return resp

    return _handle


def check_url_params(func):
    @wraps(func)
    def _handle(*k, **v):
        """
        对请求参数进行过滤或者检查处理
        """
        return func(*k, **v)

    return _handle
