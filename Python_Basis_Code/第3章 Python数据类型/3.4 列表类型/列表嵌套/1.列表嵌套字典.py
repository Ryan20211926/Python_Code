# coding:utf-8
# @Time    : 2025/4/29 13:02
# @Author  : Ryan
# @FileName: 1.列表嵌套字典.py
"""
"""
user_list = [
    {'name': 'alex', 'pwd': '123123', 'times': 1},
    {'name': 'eric', 'pwd': '123123', 'times': 1},
    {'name': 'tony', 'pwd': '123123', 'times': 1},
]
user = input('用户名：')
pwd = input('密码：')
for item in user_list:
    if user == item['name'] and pwd == item['pwd']:
        print('登录成功')
        break
else:
    print("登录失败！")


