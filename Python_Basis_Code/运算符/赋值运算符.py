# coding:utf-8
# @Time    : 2024/12/19 6:37
# @Author  : Ryan
# @FileName: 赋值运算符.py

# 基本赋值
a = 7
print(a)  # 输出 7

# 复合赋值
a = 5
a += 3
print(a)  # 输出 8

a = 5
a -= 3
print(a)  # 输出 2

a = 5
a *= 3
print(a)  # 输出 15

a = 10
a /= 2
print(a)  # 输出 5.0

a = 10
a //= 3
print(a)  # 输出 3

a = 10
a %= 3
print(a)  # 输出 1

a = 2
a **= 3
print(a)  # 输出 8

# 链式赋值
x = y = z = 10
print(x, y, z)  # 输出 10 10 10

# 解包赋值
x, y, z = 5, 3, 1
print(x, y, z)  # 输出 5 3 1