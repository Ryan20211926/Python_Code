# coding:utf-8
# @Time    : 2025/5/9 13:42
# @Author  : Ryan
# @FileName: 3.2 动态类型参数.py
"""
"""
from flask import Flask
app = Flask(__name__)

# http://127.0.0.1:5000/add/5
@app.route('/add/<int:num>')
def add(num):
    print('---->', type(num))
    result = num + 10
    return str(result)

# http://127.0.0.1:5000/add1/10.5
@app.route('/add1/<float:money>')
def add1(money):
    print('====>', type(money))
    return str(money)

# http://127.0.0.1:5000/index/some/path
@app.route('/index/<path:p>')
def get_path(p):
    print('******>', type(p))  # str类型
    print(p)
    return p

# http://127.0.0.1:5000/test/123e4567-e89b-12d3-a456-426614174000
@app.route('/test/<uuid:id>')
def test(id):
    print('#########>>', type(id))
    return f'获取唯一的标识码{id}'

if __name__ == "__main__":
    app.run(debug=True)



