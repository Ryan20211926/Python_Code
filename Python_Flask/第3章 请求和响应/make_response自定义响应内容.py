# coding:utf-8
# @Time    : 2025/5/4 17:49
# @Author  : Ryan
# @FileName: make_response自定义响应内容.py
"""
"""
from flask import Flask,make_response

app = Flask(__name__)

@app.route('/demo2')
def demo02():
    resp = make_response("make response 测试")
    resp.headers['python'] = 'hello'
    resp.status = '404 Not found'
    return resp

if __name__ == '__main__':
    app.run(debug=True)