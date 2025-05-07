# coding:utf-8
# @Time    : 2025/4/29 12:36
# @Author  : Ryan
# @FileName: 字符串编码.py
"""
"""
s = "你好"
bytes_data = s.encode('utf-8')
print(bytes_data)  # 输出: b'\xe4\xbd\xa0\xe5\xa5\xbd'，这代表"你好"的UTF-8编码
print(bytes_data.decode('utf-8'))


# 获取所有常用汉字
hanzi_list = [chr(i) for i in range(0x4e00, 0x9fa6)]
print(hanzi_list[:10])  # 打印前10个汉字


# 从文件中读取汉字
with open('hanzi.txt', 'r', encoding='utf-8') as f:
    text = f.read()
# 提取汉字
hanzi_list = [char for char in text if '\u4e00' <= char <= '\u9fff']
print(hanzi_list)  # 输出文件中的所有汉字