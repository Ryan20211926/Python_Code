# coding:utf-8
# @Time    : 2025/5/6 13:10
# @Author  : Ryan
# @FileName: 1. 基本应用.py
"""
"""

from pypinyin import pinyin, Style


# 示例汉字
hanzi = "你好世界"
# 获取拼音
pinyin_list = pinyin(hanzi, style=Style.NORMAL)
print(pinyin_list)  # 输出: [['nǐ'], ['hǎo'], ['shì'], ['jiè']]

# 带声调的拼音
print(pinyin("中文", style=Style.TONE))  # 输出：[['zhōng'], ['wén']]

# 声调用数字表示
print(pinyin("中文", style=Style.TONE2))  # 输出：[['zho1ng'], ['we2n']]

# 只取声母
print(pinyin("中文", style=Style.INITIALS))  # 输出：[['zh'], ['w']]

# 只取首字母
print(pinyin("中文", style=Style.FIRST_LETTER))  # 输出：[['z'], ['w']]