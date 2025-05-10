# coding:utf-8
# @Time    : 2025/5/10 13:27
# @Author  : Ryan
# @FileName: 3. make_response返回.py
"""
"""

from flask import Flask, make_response


app = Flask(__name__)

content = '''
<!DOCTYPE html>
<html>
<head>
    <title>京东购物网站</title>
</head>
<body>
    <h1>欢迎来到京东购物网站</h1>
    <div>
        <ul>
            <li>hello</li>
            <li>abc</li>
            <li>world</li>
        </ul>
    </div>
</body>
</html>
'''

#  http://127.0.0.1:5000/index1
@app.route('/index1')
def index1():
    response = make_response(content)
    response.content_type = 'text/html; charset=utf-8'
    return response

#  http://127.0.0.1:5000/index2
@app.route('/index2')
def index2():
    response = make_response(content)
    response.content_type = 'text/html; charset=utf-8'
    # 添加响应头
    response.headers['mytest'] = '123abc'
    return response



if __name__ == '__main__':
    app.run(debug=True)