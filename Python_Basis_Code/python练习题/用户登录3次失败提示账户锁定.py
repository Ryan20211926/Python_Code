# coding:utf-8
# @Time    : 2024/12/20 12:55
# @Author  : Ryan
# @FileName: 用户登录3次失败提示账户锁定.py
# 假设的正确用户名和密码
correct_username = "user123"
correct_password = "password123"

# 尝试登录的次数
attempts = 0

# 最大尝试次数
max_attempts = 3

while attempts < max_attempts:
    # 获取用户输入的用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")

    # 检查用户名和密码是否正确
    if username == correct_username and password == correct_password:
        print("登录成功！")
        break
    else:
        print("用户名或密码错误！")
        attempts += 1  # 增加尝试次数

    # 检查是否达到最大尝试次数
    if attempts == max_attempts:
        print("账户已被锁定。")
    else:
        print(f"请再试一次，您还有{max_attempts - attempts}次机会。")
# 如果循环结束且未登录成功，则输出账户锁定信息
if username != correct_username or password != correct_password:
    print("由于连续多次输入错误，账户已被锁定。")