# coding:utf-8
# @Time    : 2025/5/10 12:42
# @Author  : Ryan
# @FileName: 路由带斜杠.py
"""
"""
from flask import Flask

# 创建Flask应用实例
app = Flask(__name__)

# http://127.0.0.1:5000/projects 显示“The project page”。
# http://127.0.0.1:5000/projects/  ：显示“The project page”。

# 路由中定义'/'，无论请求的URL是否带有/，都可以执行视图函数 如果请求是没有/ 浏览器做了一次重定向
@app.route('/projects/')
def projects():
    return 'The project page'

# http://127.0.0.1:5000/about 显示“The about page”。
# http://127.0.0.1:5000/about/ 显示“Not Found”错误。
# 定义路由和视图函数
@app.route('/about')  # 请求路由中如果添加了/: http://127.0.0.1:5000/about/ 显示Not Found
def about():
    return 'The about page'
# http://127.0.0.1:5000/example
# http://127.0.0.1:5000/example/
@app.route('/example', strict_slashes=False)
def example():
    return "Example Page"

# http://127.0.0.1:5000/test
# http://127.0.0.1:5000/test/

@app.route('/test/', strict_slashes=False)
def test():
    return "test Page"
# 检查是否是主程序入口，如果是则启动应用
if __name__ == '__main__':
    app.run(debug=True)  # 开启debug模式，便于调试