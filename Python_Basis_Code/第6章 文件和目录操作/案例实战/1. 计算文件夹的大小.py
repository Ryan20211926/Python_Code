# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/21 6:06
# @Author  : Ryan 
# @File    : 1. 计算文件夹的大小.py
# @Software: PyCharm
"""

# 遍历文件夹中的所有文件和子文件夹。
# 获取每个文件的大小并累加。

import os

def get_folder_size(folder_path):
    """
    计算指定文件夹的总大小
    :param folder_path: 文件夹路径
    :return: 文件夹的总大小（以字节为单位）
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

# 示例：计算某个文件夹的大小
folder_path = input("请输入文件夹路径：")
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    size_in_bytes = get_folder_size(folder_path)
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024
    size_in_gb = size_in_mb / 1024

    print(f"文件夹 '{folder_path}' 的总大小为：")
    print(f"{size_in_bytes} 字节")
    print(f"{size_in_kb:.2f} KB")
    print(f"{size_in_mb:.2f} MB")
    print(f"{size_in_gb:.2f} GB")
else:
    print("错误：指定的路径不存在或不是一个文件夹")