# coding:utf-8
# @Time    : 2025/5/10 13:49
# @Author  : Ryan
# @FileName: 5. Response对象.py
"""
"""
from flask import Flask, Response

app = Flask(__name__)

@app.route('/index3')
def index3():
    response = Response('<h1>大家想好中午吃什么了吗？</h1>')  # 返回的Response对象
    print(response.content_type)  # 打印内容类型
    print(response.headers)  # 打印头部信息
    print(response.status_code)  # 打印状态码
    print(response.status)  # 打印状态描述
    return response

if __name__ == '__main__':
    app.run(debug=True)