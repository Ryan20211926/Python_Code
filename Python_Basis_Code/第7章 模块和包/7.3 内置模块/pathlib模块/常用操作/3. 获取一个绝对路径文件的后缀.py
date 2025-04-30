# coding:utf-8
# @Time    : 2025/4/29 13:10
# @Author  : Ryan
# @FileName: 3. 获取一个绝对路径文件的后缀.py
"""
"""

from pathlib import Path

if __name__=="__main__":
    # 当文件后缀只有一个点，如xxx.doc,xxx.py等，使用如下方式
    path=Path("G:/src/django/mysite1/mysite1/test.py")
    print(path.suffix)
    # 当文件后缀有多个点时，如xxx.tar.gz等，此时获取后缀需要用字符串的join方法处理一下
    path=Path("G:/src/django/mysite1/mysite1/test.tar.gz")
    print(path.suffix)
    print(path.suffixes)
    print("".join(path.suffixes))
