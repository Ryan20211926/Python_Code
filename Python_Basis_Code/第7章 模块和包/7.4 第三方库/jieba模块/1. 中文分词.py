# coding:utf-8
# @Time    : 2025/5/6 13:16
# @Author  : Ryan
# @FileName: 1. 中文分词.py
"""
"""

import jieba

# 示例文本
text = "我爱自然语言处理"
# 分词
words = jieba.lcut(text)
print(words)  # 输出: ['我', '爱', '自然', '语言', '处理']