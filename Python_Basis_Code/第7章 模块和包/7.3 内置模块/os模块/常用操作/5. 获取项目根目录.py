# coding:utf-8
# @Time    : 2025/5/4 17:31
# @Author  : Ryan
# @FileName: 5. 获取项目根目录.py
"""
"""

import os
# 获得根路径
def getRootPath(project):
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find(project) + len(project)]
    print(rootPath)
    return rootPath
def get_desktop_dir():
    """
    @Description: 获取用户桌面路径
    """
    desktop_dir =  os.path.join(os.path.expanduser('~'),'Desktop')
    print(desktop_dir)
    return desktop_dir
if __name__ == '__main__':
    get_desktop_dir()

if __name__ == '__main__':
    getRootPath("RyanProject")