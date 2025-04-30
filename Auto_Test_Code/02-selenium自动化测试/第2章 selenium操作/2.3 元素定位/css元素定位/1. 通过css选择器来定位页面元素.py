# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:26
# @Author  : Ryan 
# @File    : 1. 通过css选择器来定位页面元素.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep
import os

"""
通过css定位页面元素
"""

driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-5.html'
driver.get(html_file)

driver.find_element_by_css_selector("body > input").send_keys('css')

sleep(3)
driver.quit()