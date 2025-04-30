# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 22:08
# @Author  : Ryan 
# @File    : 1. 模拟选中复选框.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/clicks.htm")
ele = driver.find_element_by_xpath("/html/body/ul//input")
ele.click()
# driver.find_element_by_xpath("/html/body/form/input[3]").submit()
sleep(2)
if ele.is_selected():
    print('pass')
sleep(2)
ele.send_keys(Keys.SPACE)
sleep(2)
driver.quit()