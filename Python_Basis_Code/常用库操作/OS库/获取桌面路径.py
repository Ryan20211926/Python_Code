# coding:utf-8
# @Time    : 2024/12/2 22:31
# @Author  : Ryan
# @FileName: 获取桌面路径.py
import os
def get_desktop_dir():
    """
    @Description: 获取用户桌面路径
    """
    desktop_dir =  os.path.join(os.path.expanduser('~'),'Desktop')
    print(desktop_dir)
    return desktop_dir
if __name__ == '__main__':
    get_desktop_dir()