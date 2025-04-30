# coding:utf-8
# @Time    : 2024/12/19 6:38
# @Author  : Ryan
# @FileName: 关系运算符.py

# 等于
print(5 == 3)  # 输出 False
print(6 == 6)  # 输出 True

# 不等于
print(5 != 3)  # 输出 True
print(6 != 6)  # 输出 False

# 大于
print(7 > 3)  # 输出 True
print(2 > 10)  # 输出 False

# 小于
print(3 < 7)  # 输出 True
print(10 < 5)  # 输出 False

# 大于等于
print(7 >= 3)  # 输出 True
print(2 >= 10)  # 输出 False

# 小于等于
print(3 <= 7)  # 输出 True
print(10 <= 5)  # 输出 False

# 身份运算符
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # 输出 False
print(a is a)  # 输出 True

# 非身份运算符
print(a is not b)  # 输出 True
print(a is not a)  # 输出 False