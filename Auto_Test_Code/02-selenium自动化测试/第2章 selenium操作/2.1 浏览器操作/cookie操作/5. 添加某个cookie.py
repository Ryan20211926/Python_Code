# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:37
# @Author  : Ryan 
# @File    : 5. 添加某个cookie.py
# @Software: PyCharm
"""
from selenium import webdriver

url = 'http://www.baidu.com/'
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)
print(len(driver.get_cookies()))  # 添加前cookies数量
driver.add_cookie({"name":"STORM","value":"123456"})
print(len(driver.get_cookies()))  # 添加后cookies数量
driver.quit()
