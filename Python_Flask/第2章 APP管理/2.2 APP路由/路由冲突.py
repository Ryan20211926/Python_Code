# coding:utf-8
# @Time    : 2025/5/7 13:37
# @Author  : Ryan
# @FileName: 路由冲突.py
"""
"""

from flask import Flask

# 创建 Flask 应用
app = Flask(__name__)
@app.route('/example')
def example1():
    return "Example 1"

@app.route('/example')
def example2():
    return "Example 2"

if __name__ == '__main__':
    app.run()