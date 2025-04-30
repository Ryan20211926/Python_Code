# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:35
# @Author  : Ryan 
# @File    : 2. 获取单个cookie.py
# @Software: PyCharm
"""
from selenium import webdriver

url = 'http://www.baidu.com/'
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)
baidu_id_cookie = driver.get_cookie('BAIDUID') # 获取'BAIDUID'cookie
print(type(baidu_id_cookie))  # 打印类型
print(baidu_id_cookie) # 打印值
driver.quit()
