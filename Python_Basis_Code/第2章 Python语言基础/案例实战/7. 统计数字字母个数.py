# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:46
# @Author  : Ryan 
# @File    : 7. 统计数字字母个数.py
# @Software: PyCharm
"""
import string


def count_characters(text):
    """
    统计文本中的数字、字母和标点符号的数量
    :param text: 输入的文本
    :return: 字典，包含数字、字母和标点符号的数量
    """
    counts = {
        'digits': 0,
        'letters': 0,
        'punctuation': 0
    }

    for char in text:
        if char.isdigit():
            counts['digits'] += 1
        elif char.isalpha():
            counts['letters'] += 1
        elif char in string.punctuation:
            counts['punctuation'] += 1
    # 输出结果
    print(f"数字的数量：{counts['digits']}")
    print(f"字母的数量：{counts['letters']}")
    print(f"标点符号的数量：{counts['punctuation']}")
    return counts

# 如果你需要统计其他类型的字符（如空格、换行符等），可以进一步扩展 count_characters 函数。
def count_characters2(text):
    counts = {
        'digits': 0,
        'letters': 0,
        'punctuation': 0,
        'spaces': 0,
        'others': 0
    }

    for char in text:
        if char.isdigit():
            counts['digits'] += 1
        elif char.isalpha():
            counts['letters'] += 1
        elif char in string.punctuation:
            counts['punctuation'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        else:
            counts['others'] += 1
    # 输出结果
    print(f"数字的数量：{counts['digits']}")
    print(f"字母的数量：{counts['letters']}")
    print(f"标点符号的数量：{counts['punctuation']}")
    print(f"空格的数量：{counts['spaces']}")
    print(f"其他字符的数量：{counts['others']}")

    return counts




if __name__ == '__main__':

    # 输入文本
    text = input("请输入一段文本：") # Hello, World! 123
    # 统计字符
    result = count_characters(text)
    print("-"*20)
    result = count_characters2(text)

