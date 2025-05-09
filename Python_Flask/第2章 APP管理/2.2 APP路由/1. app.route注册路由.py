# coding:utf-8
# @Time    : 2025/5/9 13:15
# @Author  : Ryan
# @FileName: 1. app.route注册路由.py

from flask import Flask,request,url_for
app = Flask(__name__)
@app.route('/') # 路由
def home():  # 视图函数
    return f"Hello"

@app.route('/about')
def about():
    return "This is the About page."

if __name__ == '__main__':
    app.run(debug=True)