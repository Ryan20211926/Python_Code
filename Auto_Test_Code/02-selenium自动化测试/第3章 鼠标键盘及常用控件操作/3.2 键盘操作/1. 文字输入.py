# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:55
# @Author  : Ryan 
# @File    : 1. 文字输入.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.find_element_by_id('kw').send_keys('storm') # 输入文字
sleep(3)
driver.quit()