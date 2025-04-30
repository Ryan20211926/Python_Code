# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 12:14
# @Author  : Ryan 
# @File    : 1. 猜数字.py
# @Software: PyCharm
"""

# 猜数字，最多猜5次。每次错误之后，提醒剩余次数
print("开始")
for x in range(1,6):
    num = input("数字：")
    if num == "666":
        print("猜对了")
        break
    else:
        message = f"猜错了，剩余次数{5 - x}"
        print(message)
print("结束")