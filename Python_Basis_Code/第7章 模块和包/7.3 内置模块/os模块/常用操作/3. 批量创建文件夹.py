# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 22:22
# @Author  : Ryan 
# @File    : 3. 批量创建文件夹.py
# @Software: PyCharm
"""
"""
import os
dir_name ="测试"
dir_number =10

if os.path.exists(dir_name):
    for i in range(dir_number):
        path_name = f'{dir_name}/销售{i}区数据/第{i}个城市数据'
        print(f"删除文件夹 '{path_name}'")
        os.removedirs(path_name)
else:
    # 创建单个文件夹
    os.mkdir(dir_name)
    for i in range(dir_number):
        path_name = f'{dir_name}/销售{i}区数据/第{i}个城市数据'
        print(f"创建文件夹 '{path_name}'")
        os.makedirs(path_name)

# 查看创建的文件夹
print('查看创建的所有文件夹')
print(os.listdir(dir_name))