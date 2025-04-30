# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:53
# @Author  : Ryan 
# @File    : 3. 页面截图返回base64的字符串.py
# @Software: PyCharm
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
a = driver.get_screenshot_as_base64()  # 当前窗口截图，输入截图对应base64的字符信息
print(type(a))
print(a)
driver.quit()