# coding:utf-8
# @Time    : 2024/12/2 22:40
# @Author  : Ryan
# @FileName: 获取当前文件的上上级目录.py
import os
base_path = os.path.dirname(os.path.dirname(__file__))
print(base_path)