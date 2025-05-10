# coding:utf-8
# @Time    : 2025/5/10 13:26
# @Author  : Ryan
# @FileName: 2. Response返回.py
"""
"""

from flask import Flask, Response

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由和视图函数

# http://127.0.0.1:5000/index1
@app.route('/index1')
def index1():
    return Response('<h1>大家想好中午吃什么了吗？</h1>')

# http://127.0.0.1:5000/index2
@app.route('/index2')
def index2():
    return Response('<h1>大家想好中午吃什么了吗？</h1>',headers={'X-Custom-Header': 'Custom Value'})

# http://127.0.0.1:5000/index3
@app.route('/index3')
def index3():
    return Response('<h1>大家想好中午吃什么了吗？</h1>', content_type='text/html')


# http://127.0.0.1:5000/index4
@app.route('/index4')
def index4():
    content = '<h1>大家想好中午吃什么了吗？</h1>'
    # 解决中文乱码的问题
    response = Response(content, content_type='text/html; charset=utf-8')
    return response

# 检查是否是主程序入口，如果是则启动应用
if __name__ == '__main__':
    app.run(debug=True)