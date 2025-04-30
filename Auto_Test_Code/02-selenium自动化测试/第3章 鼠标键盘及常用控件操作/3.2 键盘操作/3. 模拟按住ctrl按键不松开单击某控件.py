# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/25 21:57
# @Author  : Ryan 
# @File    : 3. 模拟按住ctrl按键不松开单击某控件.py
# @Software: PyCharm
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/clickCombo.htm")
ele = driver.find_element_by_xpath('/html/body/div/div')
# 按下control键，不松开
ActionChains(driver).key_down(Keys.CONTROL).perform()
# 然后点击
ele.click()
sleep(3)
driver.quit()