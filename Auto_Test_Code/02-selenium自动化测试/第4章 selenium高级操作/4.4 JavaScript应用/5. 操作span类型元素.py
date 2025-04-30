# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:31
# @Author  : Ryan 
# @File    : 5. 操作span类型元素.py
# @Software: PyCharm
"""

# 通过id来定位元素 获取span的文本

from selenium import webdriver
from time import sleep
import os

'''
定位元素，通过text取文本；
'''
driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7_3.html'
driver.get(html_file)
ele = driver.find_element_by_id('span_id')
print(ele.text)
driver.quit()




# 通过javascript修改标签的文本

from selenium import webdriver
from time import sleep
import os

'''
通过js的方式修改span中间的值
js = 'document.getElementById("span_id").innerText="aaaa"'
'''
driver = webdriver.Chrome()
html_file = 'File:///' + os.getcwd() + os.sep + 'myhtml7_3.html'
driver.get(html_file)
sleep(2)
js1 = "document.getElementById('span_id').innerText='aaa'"
driver.execute_script(js1)
sleep(2)
driver.quit()
