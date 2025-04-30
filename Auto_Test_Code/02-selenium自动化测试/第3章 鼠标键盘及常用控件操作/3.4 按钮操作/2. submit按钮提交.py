# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 22:05
# @Author  : Ryan 
# @File    : 2. submit按钮提交.py
# @Software: PyCharm
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('storm')
driver.find_element_by_id('su').submit() # 对于submit按钮，可以使用submit方法
sleep(2)
driver.quit()