# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:44
# @Author  : Ryan 
# @File    : 7. 通过cookie实现免登录函数封装.py
# @Software: PyCharm
"""


# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 17:38
# @Author  : Ryan 
# @File    : 6. 使用cookie免登录163邮箱.py
# @Software: PyCharm
"""
import time
def get_url_with_cookies(driver, target_url, file):
    cookies_file_path = file
    cookies_file = open(cookies_file_path, "r")
    cookies_str = cookies_file.readline()
    cookies_dict = json.loads(cookies_str)
    time.sleep(2)
    driver.get(target_url)
    driver.delete_all_cookies()
    for cookie in cookies_dict:
        for k in cookie.keys():
            if k == "expiry":
                cookie[k] = int(cookie[k])
    driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()

if __name__ == "__main__":
    from selenium import webdriver
    from time import sleep
    import json
    driver = webdriver.Chrome()
    target_url= 'http://mail.163.com/'
    get_url_with_cookies(driver,target_url,"mycookie.json")
    sleep(3)
    driver.quit()

