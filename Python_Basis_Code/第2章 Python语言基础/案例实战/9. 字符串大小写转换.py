# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:52
# @Author  : Ryan 
# @File    : 9. 字符串大小写转换.py
# @Software: PyCharm
"""
# 将字符串中的所有小写字母转换为大写字母
def to_uppercase(s):
    result = []
    for char in s:
        if 'a' <= char <= 'z':  # 判断是否为小写字母
            # 转换为大写字母
            upper_char = chr(ord(char) - 32)
            result.append(upper_char)
        else:
            result.append(char)
    return ''.join(result)

# 测试
input_str = input("请输入一个字符串：")
print("转换为大写后的字符串：", to_uppercase(input_str))


# 将字符串中的所有大写字母转换为小写字母
def to_lowercase(s):
    result = []
    for char in s:
        if 'A' <= char <= 'Z':  # 判断是否为大写字母
            # 转换为小写字母
            lower_char = chr(ord(char) + 32)
            result.append(lower_char)
        else:
            result.append(char)
    return ''.join(result)

# 测试
input_str = input("请输入一个字符串：")
print("转换为小写后的字符串：", to_lowercase(input_str))


# 切换字符串中的大小写（大写转小写，小写转大写）
def swap_case(s):
    result = []
    for char in s:
        if 'a' <= char <= 'z':  # 判断是否为小写字母
            # 转换为大写字母
            upper_char = chr(ord(char) - 32)
            result.append(upper_char)
        elif 'A' <= char <= 'Z':  # 判断是否为大写字母
            # 转换为小写字母
            lower_char = chr(ord(char) + 32)
            result.append(lower_char)
        else:
            result.append(char)
    return ''.join(result)

# 测试
input_str = input("请输入一个字符串：")
print("切换大小写后的字符串：", swap_case(input_str))