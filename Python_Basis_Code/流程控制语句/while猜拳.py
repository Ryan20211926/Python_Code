# coding:utf-8
# @Time    : 2024/12/20 7:00
# @Author  : Ryan
# @FileName: while猜拳.py

import random

# 定义可能的选择
choices = ["石头", "剪刀", "布"]

# 游戏规则映射
rules = {
    "石头": "剪刀",
    "剪刀": "布",
    "布": "石头"
}

# 游戏主循环
while True:
    # 用户输入
    user_choice = input("请选择 石头、剪刀 或 布 (输入'退出'结束游戏)：")
    if user_choice == "退出":
        print("游戏结束，感谢您的参与！")
        break

    # 验证用户输入
    if user_choice not in choices:
        print("无效的输入，请输入 石头、剪刀 或 布。")
        continue

    # 计算机随机选择
    computer_choice = random.choice(choices)
    print(f"计算机选择了：{computer_choice}")

    # 判断胜负
    if user_choice == computer_choice:
        print("平局！")
    elif rules[user_choice] == computer_choice:
        print("你赢了！")
    else:
        print("你输了！")

    # 询问是否继续
    continue_game = input("是否要再玩一次？(是/否)：")
    if continue_game.lower() != "是":
        print("游戏结束，感谢您的参与！")
        break