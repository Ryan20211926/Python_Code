# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:39
# @Author  : Ryan 
# @File    : 1. 指定浏览器最大化启动.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(2)
driver.quit()