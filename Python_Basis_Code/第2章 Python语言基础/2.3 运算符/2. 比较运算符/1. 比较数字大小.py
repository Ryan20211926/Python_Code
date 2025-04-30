# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:35
# @Author  : Ryan 
# @File    : 1. 比较数字大小.py
# @Software: PyCharm
"""
# 输入三个数字
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))
c = float(input("请输入第三个数字："))

# 比较三个数字的大小
if a >= b and a >= c:
    largest = a
    if b >= c:
        middle = b
        smallest = c
    else:
        middle = c
        smallest = b
elif b >= a and b >= c:
    largest = b
    if a >= c:
        middle = a
        smallest = c
    else:
        middle = c
        smallest = a
else:
    largest = c
    if a >= b:
        middle = a
        smallest = b
    else:
        middle = b
        smallest = a

# 输出结果
print(f"最大的数字是：{largest}")
print(f"中间的数字是：{middle}")
print(f"最小的数字是：{smallest}")