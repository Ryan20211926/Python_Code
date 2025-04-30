# coding:utf-8
# @Time    : 2024/12/20 7:04
# @Author  : Ryan
# @FileName: while猜数字.py

import random

# 随机生成一个1到100之间的数字
secret_number = random.randint(1, 100)
guess_count = 0
user_guess = None

print("猜数字游戏开始！我已经想好了一个1到100之间的数字。")

while user_guess != secret_number:
    user_guess = int(input("请输入你的猜测（1-100）："))
    guess_count += 1

    if user_guess < secret_number:
        print("太低了，再试试看。")
    elif user_guess > secret_number:
        print("太高了，再试试看。")

# 判断猜测次数并给出提示
if guess_count == 1:
    print("运气真好！一次就猜中了，建议买彩票哦！")
else:
    print(f"猜了{guess_count}次，终于猜对了！")

print("游戏结束，感谢参与！")