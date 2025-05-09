# coding:utf-8
# @Time    : 2025/5/9 13:01
# @Author  : Ryan
# @FileName: 3. 动态路由.py
"""
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '我是首页'

# 这里的变量名称要与视图函数中的变量名称一致 否则会报错
# @app.route("/city/<city_name>")
@app.route("/city/<name>")
def get_city_name(name):
    return f"这里是{name}城市"

# 假设从数据库中获取了以下 ID
item_ids = [1, 2, 3]
@app.route('/item/<int:item_id>')
def dynamic_view(item_id):
    return f"Item ID: {item_id}"

data = {'a': '北京', 'b': '上海', 'c': '深圳'}
@app.route('/get_city/<key>')
def get_city(key):
    print(type(key))
    return data.get(key)



if __name__ == '__main__':
    app.run(debug=True)



