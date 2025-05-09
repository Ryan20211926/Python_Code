# coding:utf-8
# @Time    : 2025/5/9 13:23
# @Author  : Ryan
# @FileName: 3.1 add_url_rule实现动态路由.py
"""
"""
from flask import Flask

app = Flask(__name__)

# 假设这是从数据库或其他数据源获取的城市列表
cities = ['北京', '上海', '深圳']
def show_city(city=None):
    if city is None:
        return '请提供城市名称'
    # 这里可以添加逻辑来获取城市的具体信息
    # 例如，从数据库中查询城市信息
    return f'这是 {city} 的信息'
# 为每个城市动态添加路由
for city in cities:
    app.add_url_rule(
        f'/city/{city}',  # 路由路径
        view_func=show_city,  # 视图函数
        defaults={'city': city},  # 默认参数
        methods=['GET']  # 支持的方法，默认是 ['GET']
    )

if __name__ == '__main__':
    app.run(debug=True)