# coding:utf-8
# @Time    : 2024/12/19 13:29
# @Author  : Ryan
# @FileName: 用户登录记住密码.py

# 假设的正确用户名和密码
correct_username = "admin"
correct_password = "password123"

# 获取用户输入的用户名和密码
username = input("请输入用户名：")
password = input("请输入密码：")

# 询问用户是否记住密码
remember_password = input("是否记住密码？(yes/no)：")

# 检查用户名和密码是否正确
if username == correct_username and password == correct_password:
    print("登录成功！")
    # 检查用户是否选择记住密码
    if remember_password.lower() == 'yes':
        print("记住密码")
    else:
        print("未记住密码")
else:
    print("用户名或密码错误！")