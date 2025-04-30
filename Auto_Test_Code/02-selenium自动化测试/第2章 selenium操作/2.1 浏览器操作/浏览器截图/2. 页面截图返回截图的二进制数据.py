# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:52
# @Author  : Ryan 
# @File    : 2. 页面截图返回截图的二进制数据.py
# @Software: PyCharm
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
a = driver.get_screenshot_as_png()  # 截图，返回截图文件的二进制数据
print(type(a))
print(a)
driver.quit()