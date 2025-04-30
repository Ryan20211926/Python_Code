# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:18
# @Author  : Ryan 
# @File    : 1. 操作页面元素.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
ele1JS = "document.getElementById('kw').value='storm'"
ele2JS = "document.getElementById('su').click()"
driver.execute_script(ele1JS)
sleep(3)
driver.execute_script(ele2JS)
sleep(3)
driver.quit()
