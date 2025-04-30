# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:43
# @Author  : Ryan 
# @File    : 7. 页面加载策略.py
# @Software: PyCharm
"""
# normal 默认情况下 如果未给浏览器options提供参数 则采用normal模式 该模式下webdriver将一直等待整个页面加载完成（浏览器左上角不再转圈）
#
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #  complete
# caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps)
driver.get('https://www.ptpress.com.cn/')
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/div[2]/input').send_keys('Storm')
sleep(2)
driver.quit()

#
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps)
driver.get('https://www.ptpress.com.cn/')
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/div[2]/input').send_keys('Storm')
sleep(2)
driver.quit()


#
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
# caps["pageLoadStrategy"] = "eager"  #  interactive
caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps)
driver.get('https://www.ptpress.com.cn/')
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/div[2]/input').send_keys('Storm')
sleep(2)
driver.quit()