# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 11:58
# @Author  : Ryan 
# @File    : 2. print基本用法.py
# @Software: PyCharm
"""

# 1.参数为字符串
print("hello Python") # 双引号字符串
print('hello Python') # 单引号字符串

# 2.参数为变量
a = 1
b = 2
c = a+b
print(c)

# 3.参数为表达式 代码会先计算表达式的结果 然后再将结果输出
print(a+b+7)

# 4.参数为多个参数 多个参数之间使用英文的逗号分隔
print("Hello", "World", "Python")

# 5.输出末尾设置
print("Hello", end=" ") # 末尾空格
print("World")
# 输出：Hello World

# 6. 参数为函数
print(dir(__file__))