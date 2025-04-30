# coding:utf-8
# @Time    : 2024/12/22 8:03
# @Author  : Ryan
# @FileName: 字典数据保存.py

# 创建一个空字典来存储书籍信息
book = {}

# 添加书名、价格、作者和出版社信息
book['书名'] = 'Python编程'
book['价格'] = 120.0  # 假设价格单位是元
book['作者'] = '某作者'
book['出版社'] = '某出版社'

# 应用促销折扣
book['价格'] *= 0.8  # 8折优惠

# 打印最终字典中的内容
print(book)