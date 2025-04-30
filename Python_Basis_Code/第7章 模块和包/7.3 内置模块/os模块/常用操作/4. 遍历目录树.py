# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/28 6:25
# @Author  : Ryan 
# @File    : 4. 遍历目录树.py
# @Software: PyCharm
"""
"""
import os

# 指定要遍历的目录路径
pathName = 'data'

print('利用walk查看data目录下的所有子文件夹以及文件。')
print('-----------')
for root, dirnames, filenames in os.walk(pathName):
    print(f'当前目录：{root}')
    print(f'它的子文件夹列表：{dirnames}')
    print(f'它包含的文件列表：{filenames}')
    print('-----------')