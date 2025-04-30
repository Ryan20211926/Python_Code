# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:54
# @Author  : Ryan 
# @File    : 4. 截取指定元素.py
# @Software: PyCharm
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.find_element_by_id('su').screenshot('d:\\A\\button.png') # 定位元素，然后截图
driver.quit()

