# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:28
# @Author  : Ryan 
# @File    : 4. 打印九九乘法表.py
# @Software: PyCharm
"""
# 打印 99 乘法表
for i in range(1, 10):  # 外层循环控制行数，从 1 到 9
    for j in range(1, i + 1):  # 内层循环控制每行的列数，从 1 到当前行数 i
        print(f"{j}x{i}={i * j}", end="\t")  # 使用 format 2.6 格式化输出，\t 用于对齐
    print()  # 每完成一行后换行