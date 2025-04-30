# coding:utf-8
# @Time    : 2024/12/2 22:25
# @Author  : Ryan
# @FileName: 获得文件当前所在路径.py
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
