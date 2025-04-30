# coding:utf-8
# @Time    : 2024/12/18 21:55
# @Author  : Ryan
# @FileName: 布尔类型转换.py
# 直接转换
print(bool(1))  # True
print(bool(0))  # False
print(bool("Hello"))  # True
print(bool(""))  # False

# 空值转换
print(bool(None))  # False
print(bool([]))  # False
print(bool({}))  # False

# 非空值转换
print(bool([1, 2, 3]))  # True
print(bool({"key": "value"}))  # True

# 数字转换
print(bool(0))  # False
print(bool(10))  # True

# 比较操作符
print(5 > 3)  # True
print(5 < 3)  # False

# 逻辑操作符
print(True and False)  # False
print(True or False)  # True
print(not True)  # False