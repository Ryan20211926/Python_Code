# coding:utf-8
# @Time    : 2025/5/4 17:36
# @Author  : Ryan
# @FileName: 6. 获取文件路径.py
"""
"""

import os
# 获取文件上上级路径
base_path = os.path.dirname(os.path.dirname(__file__))
print(base_path)

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
def get_current_path():
    print(os.path.dirname(__file__))
if __name__ == '__main__':
    # resource_path()
    get_current_path()