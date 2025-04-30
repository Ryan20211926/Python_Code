# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:40
# @Author  : Ryan 
# @File    : 2. 获取元素的属性信息.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
ele1 = driver.find_element_by_id('su') # 通过id定位百度搜索按钮
ele2 = driver.find_element_by_id('kw') # 通过id定位百度输入框

print(ele1.get_attribute('id'))  #打印搜索按钮的id属性
print(ele2.get_attribute('name')) #打印输入框的name属性
print(ele1.get_attribute('value')) #打印按钮的文字，其实就是value属性
print(type(ele1.get_attribute('name')))
print(ele1.get_attribute('name'))

driver.quit()