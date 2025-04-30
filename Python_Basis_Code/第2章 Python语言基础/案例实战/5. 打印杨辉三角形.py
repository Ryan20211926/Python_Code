# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:29
# @Author  : Ryan 
# @File    : 5. 打印杨辉三角形.py
# @Software: PyCharm
"""
def print_pascals_triangle(n):
    """
    打印杨辉三角形
    :param n: 三角形的行数
    """
    triangle = []  # 用于存储杨辉三角形的每一行

    for i in range(n):
        row = [1] * (i + 1)  # 创建当前行，初始值为1
        # 计算当前行的值（除了第一个和最后一个1）
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # 将当前行添加到三角形中

    # 打印杨辉三角形
    for row in triangle:
        print(" ".join(map(str, row)).center(n * 4))  # 使用 center 方法居中对齐

# 调用函数，打印杨辉三角形
n = int(input("请输入杨辉三角形的行数："))
print_pascals_triangle(n)