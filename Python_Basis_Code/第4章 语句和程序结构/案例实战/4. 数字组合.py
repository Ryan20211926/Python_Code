# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 11:22
# @Author  : Ryan 
# @File    : 4. 数字组合.py
# @Software: PyCharm
"""

# 使用数字 1、2、3、4 组合成不同的三位数

# 定义数字列表
digits = [1, 2, 3, 4]

# 用于存储生成的三位数
unique_numbers = set()

# 嵌套的 for 循环生成所有可能的三位数
for i in digits:
    for j in digits:
        for k in digits:
            # 确保 i、j、k 互不相同
            if i != j and i != k and j != k:
                # 组合成三位数
                number = i * 100 + j * 10 + k
                # 添加到集合中去重
                unique_numbers.add(number)

# 打印所有不同的三位数
print("所有不同的三位数：")
for number in sorted(unique_numbers):  # 排序后打印
    print(number)


import itertools

# 定义数字列表
digits = [1, 2, 3, 4]

# 生成所有三位数的排列
permutations = itertools.permutations(digits, 3)

# 将排列转换为整数并打印
unique_numbers = set()  # 使用集合去重
for perm in permutations:
    number = int(''.join(map(str, perm)))  # 将排列转换为整数
    unique_numbers.add(number)  # 添加到集合中

# 打印所有不同的三位数
print("所有不同的三位数：")
for number in sorted(unique_numbers):  # 排序后打印
    print(number)