# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/18 22:49
# @Author  : Ryan 
# @File    : ryan_files.py
# @Software: PyCharm
from utils.ryan_log import  ApiAutoLog
logger = ApiAutoLog()
import os
import random
# 获得根路径
def getRootPath(project):
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find(project) + len(project)]
    logger.info(f"项目的跟目录{rootPath}")
    return rootPath
# 从根目录下开始获取其他路径
def getOtherPath(project,abspath:str):
    #调用了上述获得项目根目录的方法
    rootPath = getRootPath(project)
    dataPath = os.path.abspath(rootPath +os.sep+abspath)
    print(dataPath)
    return dataPath
def get_random_str(min_number, max_number):
    return str(random.randint(int(min_number), int(max_number)))



if __name__ == '__main__':
    getRootPath("RyanProject")
    # getOtherPath("RyanProject","data")