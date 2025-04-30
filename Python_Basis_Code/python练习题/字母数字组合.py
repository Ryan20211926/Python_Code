# coding:utf-8
# @Time    : 2024/12/21 15:20
# @Author  : Ryan
# @FileName: 字母数字组合.py

import random
import string

def generate_random_string(length):
    # 包含所有字母和数字的字符串
    characters = string.ascii_letters + string.digits
    # 随机选择字符生成字符串
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

# 调用函数生成一个长度为10的随机字符串
random_str = generate_random_string(10)
print(random_str)