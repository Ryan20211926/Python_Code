# coding:utf-8
# @Time    : 2024/12/21 15:37
# @Author  : Ryan
# @FileName: 用户登录验证.py

import re

# 假设这是存储用户名和密码的数据库
user_database = {
    'user123': '123456',  # 示例用户名和密码
    '12345678901': '123456'  # 示例手机号码和密码
}

def is_valid_username(username):
    # 检查用户名是否全部小写，首字母不能是数字，长度必须6位以上
    return username.islower() and not username[0].isdigit() and len(username) >= 6

def is_valid_phone_number(phone_number):
    # 检查手机号码是否为纯数字且长度为11
    return re.match(r'^\d{11}$', phone_number) is not None

def is_valid_password(password):
    # 检查密码是否为6位数字
    return re.match(r'^\d{6}$', password) is not None

def login():
    while True:
        username_or_phone = input("请输入用户名或手机号码：")
        if username_or_phone.lower() == 'exit':  # 用户选择退出
            print("退出程序。")
            break

        if is_valid_username(username_or_phone) or is_valid_phone_number(username_or_phone):
            password = input("请输入密码：")
            if is_valid_password(password):
                if username_or_phone in user_database and user_database[username_or_phone] == password:
                    print("登录成功")
                    return True
                else:
                    print("用户名或手机号码与密码不匹配")
            else:
                print("密码必须是6位数字")
        else:
            print("用户名或手机号码不符合条件")

        # 询问用户是否重试
        retry = input("是否重新尝试登录？(yes/no): ")
        if retry.lower() != 'yes':
            print("退出程序。")
            break

# 调用登录函数
login()