# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 21:32
# @Author  : Ryan 
# @File    : 4. 获取桌面路径.py
# @Software: PyCharm
"""
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