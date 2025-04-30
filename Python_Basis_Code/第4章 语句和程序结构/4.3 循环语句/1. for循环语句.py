# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 18:29
# @Author  : Ryan 
# @File    : 1. for循环语句.py
# @Software: PyCharm
"""

# 打印1-10
for i in range(1, 11):  # range(1, 11)生成从1到10的数字
    print(i)


# 累加1-50
# 初始化累加器
sum = 0
# 使用for循环从1到50进行累加
for i in range(1, 51):
    sum += i
# 打印最终的累加结果
print("从1到50的累加和是:", sum)