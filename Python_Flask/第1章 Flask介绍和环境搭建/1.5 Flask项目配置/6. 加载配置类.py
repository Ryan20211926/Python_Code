# coding:utf-8
# @Time    : 2025/5/7 13:38
# @Author  : Ryan
# @FileName: 6. 加载配置类.py
"""
"""
# app.py
from flask import Flask

# 创建 Flask 应用
app = Flask(__name__)

# 选择要加载的配置
# 例如，加载开发环境配置
app.config.from_object('config.DevelopmentConfig')

# 打印配置以验证
print("DEBUG:", app.config['DEBUG'])
print("SECRET_KEY:", app.config['SECRET_KEY'])
print("SQLALCHEMY_DATABASE_URI:", app.config['SQLALCHEMY_DATABASE_URI'])

# 定义一个简单的路由
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 启动 Flask 应用
if __name__ == '__main__':
    app.run()