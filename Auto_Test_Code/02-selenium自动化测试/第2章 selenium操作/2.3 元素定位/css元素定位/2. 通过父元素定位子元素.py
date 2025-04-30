# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:27
# @Author  : Ryan 
# @File    : 2. 通过父元素定位子元素.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep
import os

"""
通过css定位页面元素
"""

driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-6.html'
driver.get(html_file)

#通过父元素parent定位子元素brother1:nth-child()
mytext = driver.find_element_by_css_selector("div#parent div:nth-child(2)").text
print(mytext)


driver.quit()