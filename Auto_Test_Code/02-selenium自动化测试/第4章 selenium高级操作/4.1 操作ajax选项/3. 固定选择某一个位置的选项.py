# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:20
# @Author  : Ryan 
# @File    : 3. 固定选择某一个位置的选项.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.sogou.com/')
driver.find_element_by_id('query').send_keys('storm')
sleep(1)
sercont = driver.find_element_by_xpath('//*[@id="vl"]/div[1]/ul/li[2]').click() # li[2]选择第二项
sleep(5)
driver.quit()


