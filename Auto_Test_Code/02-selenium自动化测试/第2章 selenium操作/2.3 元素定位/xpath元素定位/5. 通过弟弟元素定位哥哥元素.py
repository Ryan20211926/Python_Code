# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:23
# @Author  : Ryan 
# @File    : 5. 通过弟弟元素定位哥哥元素.py
# @Software: PyCharm
"""
from selenium import webdriver
import os

"""
通过弟弟定位哥哥
"""

driver = webdriver.Chrome()
html_file = os.getcwd() + os.sep + 'myhtml5-4.html'
driver.get(html_file)

# 1.xpath,通过父节点获取其哥哥节点
mytext = driver.find_element_by_xpath("//div[@id='D']/../div[1]").text
print(mytext)

# 2.xpath轴 preceding-sibling
mytext1 = driver.find_element_by_xpath("//div[@id='D']/preceding-sibling::div[1]").text
print(mytext1)

driver.quit()