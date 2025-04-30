# coding:utf-8
# @Time    : 2025/4/29 13:13
# @Author  : Ryan
# @FileName: 5. 路径拼接.py
"""
"""
# 方式1：初始化Path实例的时候直接使用多个目录，如：
from pathlib import Path

if __name__=="__main__":
    path=Path("G:/","src/django","mysite1","mysite1","test.tar.gz")
    print(path)

# 方式2：使用joinpath方法
from pathlib import Path
if __name__=="__main__":
    path=Path("G:/src/django/mysite1")
    path=path.joinpath("mysite1/test.tar.gz")
    print(path)

# 方式3：直接拼接
from pathlib import Path

if __name__=="__main__":
    path=Path("G:/src/django/mysite1")
    path=path / "mysite1/test.tar.gz"
    print(path)