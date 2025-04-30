# coding:utf-8
# @Time    : 2025/4/29 13:12
# @Author  : Ryan
# @FileName: 4. 获取一个路径的上层目录，上上层目录，上上上层目录.py
"""
"""
from pathlib import Path

if __name__=="__main__":
    path=Path("G:/src/django/mysite1/mysite1/test.tar.gz")
    print(path.parent)
    print(path.parent.parent)
    print(path.parent.parent.parent)