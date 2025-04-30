# coding:utf-8
# @Time    : 2024/12/20 13:08
# @Author  : Ryan
# @FileName: 猜骰子得金币.py

import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_game(gold, games_played):
    print(f"开始游戏之旅，当前金币{gold}")
    answer = input("是否开始游戏(Y/N)?").lower()
    while gold >= 5 and answer == "y":
        gold -= 5  # 消耗5个金币
        total = roll_dice()
        print(f"骰子点数之和为: {total}")
        guess = input("洗牌完毕，请猜大小（大/小）").strip().lower()
        if total <= 4 and guess == '小' or total > 4 and guess == '大':
            gold += 2  # 猜对获得2枚金币
            print("猜对了，获得2枚金币。")
        else:
            print("猜错了，没有奖励。")
        games_played += 1
        answer = input("是否继续游戏(Y/N)?").lower()
        if answer == "n":
            print(f"结束游戏之旅，当前金币{gold}")
            print(f"游戏结束，您总共玩了 {games_played} 局。")
            break

def recharge(gold):
    while True:
        amount = int(input("请输入充值金额:"))
        if amount % 10 == 0:
            gold += amount // 10 * 20  # 每10元获得20个金币
            print(f"充值成功，当前金币：{gold}")
            play_game(gold,games_played)
            break
        else:
            print("充值失败，充值金额必须是10元的倍数。")
if __name__ == '__main__':
    # 初始金币
    gold = random.randint(1,10)
    # 游戏主循环
    games_played = 0
    print(f"游戏开始前的金币{gold}")
    if gold < 5:
        print(f"金币不足请充值再玩！")
        recharge(gold)
    else:
        play_game(gold,games_played)
        # play_game(gold,games_played)
    # answer = input("是否开始游戏（y/n）?").lower()
    # if gold >= 5 and answer =="y":
    #     play_game(gold,games_played)
    # elif gold <5 and answer == "y":
    #     recharge(gold)
    # else:
    # if gold < 5:
    #     recharge(gold)
    # else:
    #
    #     print(f'****************开启游戏之旅**************')
    #     gold, games_played = play_game(gold, games_played)
