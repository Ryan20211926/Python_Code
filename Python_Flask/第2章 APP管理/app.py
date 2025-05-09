# coding:utf-8
# @Time    : 2025/5/9 13:13
# @Author  : Ryan
# @FileName: app.py
"""
"""
from flask import Flask
app = Flask(__name__)
def hello():
    # 另一种 基于类的视图(也叫即插视图)
    return {'hello': 'world'}
app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    app.run(debug=True)