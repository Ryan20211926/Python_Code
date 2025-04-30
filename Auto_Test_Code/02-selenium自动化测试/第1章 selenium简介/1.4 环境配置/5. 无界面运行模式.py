# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:42
# @Author  : Ryan 
# @File    : 5. 无界面运行模式.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options = options)
driver.get('https://www.baidu.com/')
sleep(2)
driver.quit()