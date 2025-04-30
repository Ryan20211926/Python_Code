# coding:utf-8
# @Time    : 2024/12/25 12:57
# @Author  : Ryan
# @FileName: 装饰器应用-函数执行时间.py

import time
from functools import wraps

def timeit_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录函数开始执行的时间
        result = func(*args, **kwargs)  # 执行函数
        end_time = time.time()  # 记录函数结束执行的时间
        execution_time = end_time - start_time  # 计算执行时间
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@timeit_decorator
def some_function(delay):
    """一个模拟耗时操作的函数"""
    time.sleep(delay)
    return f"Function completed with a delay of {delay} seconds"

# 测试装饰器
result = some_function(2)
print(result)