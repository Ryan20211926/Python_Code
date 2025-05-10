# coding:utf-8
# @Time    : 2025/5/10 13:52
# @Author  : Ryan
# @FileName: 1. 设置cookie.py
"""
"""
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    content = '<h1>大家想好中午吃什么了吗？</h1>'
    response = Response(content)
    print(response.status)  # 打印状态码，默认为 200 OK
    response.set_cookie('name', '翔宇')  # 设置 cookie
    return response

if __name__ == '__main__':
    app.run(debug=True)