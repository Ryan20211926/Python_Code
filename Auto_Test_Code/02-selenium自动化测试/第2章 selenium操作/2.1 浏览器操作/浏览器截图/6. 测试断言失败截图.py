# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:55
# @Author  : Ryan 
# @File    : 6. 测试断言失败截图.py
# @Software: PyCharm
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('Storm')
if driver.find_element_by_id('kw').text == "storm":
    pass
else:
    driver.save_screenshot('d:\\A\\a.png')
driver.quit()