# coding:utf-8
# @Time    : 2024/12/21 20:09
# @Author  : Ryan
# @FileName: 列表字母数字标点符号统计.py
import string

def count_characters(s):
    # 初始化计数器
    letters = 0
    digits = 0
    punctuations = 0

    # 遍历字符串中的每个字符
    for char in s:
        if char.isalpha():  # 检查是否为字母
            letters += 1
        elif char.isdigit():  # 检查是否为数字
            digits += 1
        elif char in string.punctuation:  # 检查是否为标点符号
            punctuations += 1

    return letters, digits, punctuations

# 示例字符串
s = "Hello, World! 123."
letters, digits, punctuations = count_characters(s)

print(f"字母数量: {letters}")
print(f"数字数量: {digits}")
print(f"标点符号数量: {punctuations}")