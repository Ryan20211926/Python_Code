# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:38
# @Author  : Ryan 
# @File    : 6. 使用cookie免登录163邮箱.py
# @Software: PyCharm
"""
"""
通过添加cookie 可以实现免登录的效果，分为2个步骤：
1. 我们把登录后的cookie保存到一个本地文件中
2. 后续登录的时候，直接读取保存到本地的cookie文件
"""

from selenium import webdriver
from time import sleep
import json

'''
该文件用来保存cookie
'''
driver = webdriver.Chrome()
driver.get('http://mail.163.com/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id('switchAccountLogin').click()
driver.switch_to.frame(0)   #然后切到这个 iframe 页面
driver.find_element_by_name('email').send_keys('apitest333@163.com')
driver.find_element_by_name('password').send_keys('abcd1234')
driver.find_element_by_id('dologin').click()
sleep(3)
mycookies = driver.get_cookies()  # 获取全部cookie
jsoncookies = json.dumps(mycookies) # 转换成json
with open("mycookie.json", 'w') as f: # 保存到文件
    f.write(jsoncookies)
driver.quit()

from selenium import webdriver
import time
import json
from time import sleep

'''
通过导入cookies的方式来实现登录，注意刷新页面；
'''
driver = webdriver.Chrome()
driver.get("http://mail.163.com/")
cookies_file_path = "mycookie.json"
with open(cookies_file_path, "r") as f:   # 读取本地的cookie文件
    cookies_str = f.readline()
    cookies_dict = json.loads(cookies_str)

driver.delete_all_cookies()   # 删除当前网址的所有cookie
for cookie in cookies_dict:  # 循环读取cookie
    for k in cookie.keys():  # 这里要判断一下
        if k == "expiry":
            cookie[k] = int(cookie[k])  # expiry参数必须为整型 否则会报错
    driver.add_cookie(cookie)

time.sleep(2)
# 添加cookie后 需要借助refresh关键字刷新页面
driver.refresh()
sleep(5)
driver.quit()

