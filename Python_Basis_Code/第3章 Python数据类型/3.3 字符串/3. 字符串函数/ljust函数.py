# coding:utf-8
# @Time    : 2025/4/29 13:18
# @Author  : Ryan
# @FileName: ljust函数.py
"""
文本左对齐并填充右边部分（长度包含前面的值）
string.ljust(width, fillchar=None)
"""
name = 'tong'
v = name.ljust(20)
print(v)
v = name.ljust(20,'*')
print(v)
