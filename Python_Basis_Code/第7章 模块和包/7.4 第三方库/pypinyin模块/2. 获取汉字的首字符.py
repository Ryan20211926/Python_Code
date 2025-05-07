# coding:utf-8
# @Time    : 2025/5/6 13:12
# @Author  : Ryan
# @FileName: 2. 获取汉字的首字符.py
"""
"""

from pypinyin import pinyin, Style

# 获取汉字的首字母并拼接成字符串
result = pinyin("中文", style=Style.FIRST_LETTER)
first_letters = ''.join([item[0] for item in result])
print(first_letters)  # 输出：zw