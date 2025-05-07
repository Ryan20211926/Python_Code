# coding:utf-8
# @Time    : 2025/5/6 13:14
# @Author  : Ryan
# @FileName: 使用正则表达式提取汉字.py
"""
"""
# 获取所有常用汉字
hanzi_list = [chr(i) for i in range(0x4e00, 0x9fa6)]
print(hanzi_list[:10])  # 打印前10个汉字

import re

# 示例字符串
text = "Hello, 世界！Python 是一门很棒的语言。"
# 提取汉字
hanzi_list = re.findall(r'[\u4e00-\u9fff]', text)
print(hanzi_list)  # 输出: ['世', '界', '是', '一', '门', '很', '棒', '的', '语', '言', '。']