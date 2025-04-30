# coding:utf-8
# @Time    : 2025/4/29 13:15
# @Author  : Ryan
# @FileName: 6. 从文件绝对路径获取文件名.py
"""
"""
from pathlib import Path

if __name__=="__main__":
    path=Path("G:/src/django/mysite1/mysite1/test.py")
    print(path.name)
    print(path.stem)
    path = Path("G:/src/django/mysite1/mysite1/test.tar.gz")
    print(path.name)
    print(path.stem)