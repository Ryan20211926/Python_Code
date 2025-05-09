# coding:utf-8
# @Time    : 2025/5/9 13:16
# @Author  : Ryan
# @FileName: 2. add_url_rule注册路由.py
from flask import Flask,request,url_for
app = Flask(__name__)


def submit():
    if request.method == 'POST':
        return "This is a POST request"
    else:
        return "This is a GET request"

def hello_endpoint():
    return "Hello, endpoint!"

def hello():
    # 另一种 基于类的视图(也叫即插视图)
    return {'hello': 'world'}
app.add_url_rule('/hello', view_func=hello)
app.add_url_rule('/submit', view_func=submit, methods=['GET', 'POST'])
app.add_url_rule('/endpoint', endpoint='my_hello', view_func=hello_endpoint)

if __name__ == '__main__':
    app.run(debug=True)