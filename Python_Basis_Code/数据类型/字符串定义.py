# coding:utf-8
# @Time    : 2024/12/21 9:29
# @Author  : Ryan
# @FileName: 字符串定义.py
s1 ="hello"
s2 = s1
s3 ="hello"
print(id(s1),id(s2),id(s3))
x = s1[:]
print(id(x))
print(id(s1))