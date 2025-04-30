# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:19
# @Author  : Ryan 
# @File    : 2. 通过模拟匹配选项.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.sogou.com/')
driver.find_element_by_id('query').send_keys('storm')
sleep(1)
sercont = driver.find_element_by_xpath('//*[@id="vl"]/div[1]/ul/li[contains(.,"形容词")]').click()
sleep(5)
driver.quit()
