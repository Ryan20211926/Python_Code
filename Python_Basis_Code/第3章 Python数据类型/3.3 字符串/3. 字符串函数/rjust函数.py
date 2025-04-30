# coding:utf-8
# @Time    : 2025/4/29 13:17
# @Author  : Ryan
# @FileName: rjust函数.py
"""
文本右对齐并填充左边部分（长度包含后面的值）
string.rjust(width, fillchar=None)
"""
name = 'tong'
v = name.rjust(20)
print(v)
v = name.rjust(20,'*')
print(v)
