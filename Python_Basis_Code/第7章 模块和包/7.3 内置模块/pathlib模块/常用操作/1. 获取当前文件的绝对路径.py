# coding:utf-8
# @Time    : 2025/4/29 13:08
# @Author  : Ryan
# @FileName: 1. 获取当前文件的绝对路径.py
"""
"""
from pathlib import Path

if __name__=="__main__":
    path=Path(__file__).resolve()
    print(path)
