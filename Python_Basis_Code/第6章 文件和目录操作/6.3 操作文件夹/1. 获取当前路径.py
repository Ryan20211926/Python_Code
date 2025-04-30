# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 21:22
# @Author  : Ryan 
# @File    : 1. 获取当前路径.py
# @Software: PyCharm
"""

import os
# 获取当前工作目录的路径
current_path = os.getcwd()
# 输出当前路径
print(f"当前工作目录的路径是：{current_path}")
# 获取当前文件的路径
print(os.path.dirname(__file__))

import sys
import os
# 获得路径，当前文件所在路径
def resource_path():
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        # running in a bundle
        base_path = sys._MEIPASS
        print('true',base_path)
    else:
        # running live
        base_path = os.path.abspath("")
        print(base_path)
# 获取当前文件下的目录
def get_current_path():
    print(os.path.dirname(__file__))
if __name__ == '__main__':
    resource_path()
    get_current_path()