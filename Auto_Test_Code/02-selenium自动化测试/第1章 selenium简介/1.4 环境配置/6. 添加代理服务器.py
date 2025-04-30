# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 20:43
# @Author  : Ryan 
# @File    : 6. 添加代理服务器.py
# @Software: PyCharm
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxy = "proxy_host:port"
desired_capabilities = webdriver.ChromeOptions().to_capabilities()
desired_capabilities['proxy'] = {
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy,
    "noProxy": None,
    "proxyType": "MANUAL",
    "class": "org.openqa.selenium.Proxy",
    "autodetect": False
}

driver = webdriver.Chrome(desired_capabilities=desired_capabilities)