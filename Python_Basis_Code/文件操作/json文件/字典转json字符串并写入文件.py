# coding:utf-8
# @Time    : 2024/11/29 6:26
# @Author  : Ryan
# @FileName: 字典转json字符串并写入文件.py
import json
dict1 = {"name":"storm","age": 30}
print(dict1)
print(type(dict1))
# 将字典数据写入txt文件
with open("1.txt", "w") as f:
    j1 = json.dump(dict1,f)
    print(j1)
    print(type(j1))


