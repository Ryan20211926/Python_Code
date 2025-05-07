# coding:utf-8
# @Time    : 2025/5/7 13:15
# @Author  : Ryan
# @FileName: 1. 打印默认配置信息.py
"""
"""
from flask import Flask
app = Flask(__name__)
print(app.config)