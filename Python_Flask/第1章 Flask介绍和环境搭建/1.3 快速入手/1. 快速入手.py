# coding:utf-8
# @Time    : 2025/5/4 18:00
# @Author  : Ryan
# @FileName: 1. 快速入手.py
"""
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, Flask!'
if __name__ == '__main__':
    app.run()