# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 21:28
# @Author  : Ryan 
# @File    : 3. 获取当前项目根路径.py
# @Software: PyCharm
"""

# 根据项目名称获取
import os
# 获得根路径
def getRootPath(project):
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find(project) + len(project)]
    print(rootPath)
    return rootPath


if __name__ == '__main__':
    getRootPath("RyanProject")

