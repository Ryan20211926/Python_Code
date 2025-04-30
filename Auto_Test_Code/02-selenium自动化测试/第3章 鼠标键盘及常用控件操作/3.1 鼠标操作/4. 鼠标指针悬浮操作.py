# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:53
# @Author  : Ryan 
# @File    : 4. 鼠标指针悬浮操作.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/mouseover.htm")
ele = driver.find_element_by_xpath('/html/body/form/input[1]')
sleep(2)
# 通过move_to_element()来模拟鼠标的悬浮动作
ActionChains(driver).move_to_element(ele).perform()
ActionChains(driver).key_up()
sleep(3)
driver.quit()