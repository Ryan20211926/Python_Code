# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:38
# @Author  : Ryan 
# @File    : 1. 获取元素的基本信息.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/") #打开百度首页
ele = driver.find_element_by_link_text('新闻') #将新闻这个元素赋值给变量ele
# ele = driver.find_element_by_id('su')
print(ele.tag_name) #打印tagname
print(ele.text) # 打印text
print(ele.size) # 打印大小

driver.quit()