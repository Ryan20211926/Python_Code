# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:42
# @Author  : Ryan 
# @File    : 4. 禁止图片加载.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' : {
        'images' : 2
    }
}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options = options)
driver.get("http://www.baidu.com/")
sleep(2)
driver.quit()