# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:28
# @Author  : Ryan 
# @File    : 4. 高亮显示正在被操作的页面元素.py
# @Software: PyCharm
"""

from selenium import webdriver
from time import sleep

def highlightElement(driver, element):
    """
    高亮显示正在被操作的页面元素
    :param driver:
    :param element:
    :return:
    """
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,"background: green; border: 2px solid red;")

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    element = driver.find_element_by_id("some-id")
    highlightElement(driver, element)
    sleep(5)
    driver.quit()