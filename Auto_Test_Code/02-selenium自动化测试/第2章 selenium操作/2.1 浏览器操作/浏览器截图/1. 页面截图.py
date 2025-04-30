# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:50
# @Author  : Ryan 
# @File    : 1. 页面截图.py
# @Software: PyCharm
"""

# 保存a.png图片
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.save_screenshot('a.png') # 截取当前页面，当前目录，保存成png类型文件
driver.quit()


# 脚本所在目录生成一张脚本名+时间戳+.png的格式图片
from selenium import webdriver
import os
import time

script_name = os.path.basename(__file__).split('.')[0]
file_name = script_name + '_' + str(time.time()) + '.png'
# print(file_name)
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.save_screenshot(file_name) # 截取当前页面，当前目录，保存成png类型文件
driver.quit()