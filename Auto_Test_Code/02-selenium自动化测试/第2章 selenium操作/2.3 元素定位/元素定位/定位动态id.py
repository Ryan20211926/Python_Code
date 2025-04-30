# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:30
# @Author  : Ryan 
# @File    : 定位动态id.py
# @Software: PyCharm
"""

# 使用contains关键字

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.126.com/')
driver.find_element_by_link_text('密码登录').click()
sleep(2)
driver.switch_to.frame(0)
driver.find_element_by_xpath('//input[contains(@id,"auto-id-")]').send_keys('storm')
sleep(2)
driver.quit()


# 使用starts-with关键词


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.126.com/')
driver.find_element_by_link_text('密码登录').click()
sleep(2)
driver.switch_to.frame(0)
driver.find_element_by_xpath('//input[starts-with(@id,"auto-id-")]').send_keys('storm')
sleep(2)
driver.quit()