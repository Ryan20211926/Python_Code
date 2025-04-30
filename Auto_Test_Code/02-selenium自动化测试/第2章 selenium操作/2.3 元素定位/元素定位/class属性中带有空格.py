# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:27
# @Author  : Ryan 
# @File    : class属性中带有空格.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7-1.html'
driver.get(html_file)
# 使用空格前或后面的部分来定位
driver.find_element_by_class_name('hello').send_keys('Storm')
sleep(2)
driver.quit()