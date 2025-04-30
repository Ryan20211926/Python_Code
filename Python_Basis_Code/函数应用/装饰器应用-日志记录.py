# coding:utf-8
# @Time    : 2024/12/25 12:54
# @Author  : Ryan
# @FileName: 装饰器应用-日志记录.py

import logging
from functools import wraps

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 记录函数调用信息
        logging.info(f"Calling function '{func.__name__}' with args: {args} and kwargs: {kwargs}")

        # 调用原始函数
        result = func(*args, **kwargs)

        # 记录函数返回值
        logging.info(f"Function '{func.__name__}' returned {result}")

        return result

    return wrapper


@log_decorator
def add_numbers(a, b):
    return a + b


@log_decorator
def multiply_numbers(a, b):
    return a * b


# 测试装饰器
add_numbers(3, 4)
multiply_numbers(3, 4)