# coding:utf-8
# @Time    : 2025/5/10 13:03
# @Author  : Ryan
# @FileName: 1. 返回response.py
"""
"""
from flask import Flask,Response

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由和视图函数
# http://127.0.0.1:5000/index
@app.route('/index')
def index():
    return {'a': '<h1>北京</h1>', 'b': '上海', 'c': '深圳'}  # application/json

# http://127.0.0.1:5000/index1
@app.route('/index1')
def index1():
    return '<h1>北京</h1>'  # Content-Type:text/html; charset=utf-8

# http://127.0.0.1:5000/index2
@app.route('/index2')
def index2():
    # TypeError: The view function did not return a valid response tuple. The tuple must have the form (body, status, headers), (body, status), or (body, headers).
    # return ('beijing', 'shanghai', 'shenzhen', 'hello')
    return ['beijing', 'shanghai', 'shenzhen', 'hello']


# http://127.0.0.1:5000/index3
@app.route('/index3')
def index3():
    return ("hello",200)

# http://127.0.0.1:5000/index4
@app.route('/index4')
def index4():
    return "对不起  访问的网站不存在！",404


# http://127.0.0.1:5000/index5
@app.route('/index5')
def index5():
    s = '''
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
    '''
    return s, 404

# 检查是否是主程序入口，如果是则启动应用
if __name__ == '__main__':
    app.run(debug=True)