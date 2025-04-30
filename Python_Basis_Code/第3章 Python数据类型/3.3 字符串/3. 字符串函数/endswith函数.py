# coding:utf-8
# @Time    : 2025/4/29 13:20
# @Author  : Ryan
# @FileName: endswith函数.py
"""
string.startswith(prefix, start=None, end=None)
string.endswith(suffix, start=None, end=None)
参数1：需要检查的字符串
参数2：设置字符串检测的起始位置
参数3：设置字符串检测的结束位置
"""
name = 'tong'
v1 = name.startswith('to')
print(v1)
v2 = name.endswith('g')
print(v2)
v3 = name.startswith('c')
print(v3)
