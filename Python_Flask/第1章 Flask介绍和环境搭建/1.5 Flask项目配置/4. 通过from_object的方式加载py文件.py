# coding:utf-8
# @Time    : 2025/5/7 13:26
# @Author  : Ryan
# @FileName: 4. 通过from_object的方式加载py文件.py
"""
"""
# 导入配置文件
import settings

from flask import Flask
app = Flask(__name__)
app.config.from_object(settings)

if __name__ == '__main__':
    app.run()