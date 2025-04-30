# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:52
# @Author  : Ryan 
# @File    : 2. 鼠标双击操作.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/clicks.htm")
ele = driver.find_element_by_xpath('/html/body/form/input[2]')
sleep(2)
# 通过double_click()来模拟鼠标左键双击的动作
ActionChains(driver).double_click(ele).perform()
sleep(3)
driver.quit()