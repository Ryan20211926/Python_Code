# coding:utf-8
# @Time    : 2024/11/29 6:25
# @Author  : Ryan
# @FileName: 字典转json字符串.py
import json
dict1 = {"name":"storm","age": 35}
print(dict1)
print(type(dict1))
# dumps将字典转为字符串
j1 = json.dumps(dict1)
print(j1)
print(type(j1))