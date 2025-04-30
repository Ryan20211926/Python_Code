# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:41
# @Author  : Ryan 
# @File    : 3. 指定浏览器Driver地址启动.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Python\\Python36\\chromedriver.exe')
driver.get('https://www.baidu.com/')
sleep(2)
driver.quit()