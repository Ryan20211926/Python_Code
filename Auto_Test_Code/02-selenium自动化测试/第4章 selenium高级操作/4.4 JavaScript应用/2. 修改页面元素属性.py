# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:19
# @Author  : Ryan 
# @File    : 2. 修改页面元素属性.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7_2.html'
driver.get(html_file)
sleep(2)
driver.find_element_by_tag_name('input').send_keys('002020/06/06')
sleep(5)
driver.quit()


# 先删除readonly属性再来输入内容

from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7_2.html'
driver.get(html_file)
sleep(2)
js2 = "document.getElementById('id1').removeAttribute('readonly')"
driver.execute_script(js2)

driver.find_element_by_tag_name('input').send_keys('002020/06/06')
sleep(5)
driver.quit()
