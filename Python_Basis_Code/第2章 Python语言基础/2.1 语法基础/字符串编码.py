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