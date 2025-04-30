# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/28 6:21
# @Author  : Ryan 
# @File    : 1. 根据文档类型归类整理文件夹.py
# @Software: PyCharm
"""
"""

import os
import shutil

def moveFile(srcFile, fileType, srcPath, destPath):
    # 拼接文件的完整路径
    srcFile = os.path.join(srcPath, srcFile)
    # 获取文件扩展名
    fileExt = os.path.splitext(srcFile)[1]
    # 判断文件扩展名是否匹配
    if fileExt == fileType:
        # 拼接目标文件的完整路径
        destFile = os.path.join(destPath, os.path.basename(srcFile))
        # 检查目标目录是否存在，如果不存在则创建
        if not os.path.exists(destPath):
            os.makedirs(destPath)
        # 移动文件
        shutil.move(srcFile, destFile)
        print(f"文件 {srcFile} 已移动到 {destFile}")

# 源文件夹路径
srcPath = 'F:\\'
# 目标文件夹路径
DirPPT = 'F:\\PPT'
DirWord = 'F:\\Word'
DirExcel = 'F:\\Excel'
DirPic = 'F:\\Pic'
DirText = 'F:\\Text'

# 获取源文件夹中的所有文件
allFile = os.listdir(srcPath)

# 将不同类型的文件移动到指定文件夹下
for i in allFile:
    moveFile(i, '.pptx', srcPath, DirPPT)
    moveFile(i, '.docx', srcPath, DirWord)
    moveFile(i, '.xlsx', srcPath, DirExcel)
    moveFile(i, '.png', srcPath, DirPic)
    moveFile(i, '.txt', srcPath, DirText)