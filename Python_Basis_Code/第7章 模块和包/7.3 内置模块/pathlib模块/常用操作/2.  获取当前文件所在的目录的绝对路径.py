# coding:utf-8
# @Time    : 2025/4/29 13:09
# @Author  : Ryan
# @FileName: 2.  获取当前文件所在的目录的绝对路径.py
"""
"""
from pathlib import Path

if __name__=="__main__":
    path=Path(__file__).resolve().parent
    print(path)