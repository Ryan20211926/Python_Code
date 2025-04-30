# coding:utf-8
# @Time    : 2024/12/19 6:46
# @Author  : Ryan
# @FileName: 输入考试分数 判断成绩是否在100-80之间.py

# 获取用户输入的考试分数
score = input("请输入你的考试分数：")

try:
    # 将输入的分数转换为整数
    score = int(score)

    # 判断成绩是否在100到80之间
    if 100 >= score >= 80:
        print("成绩在100到80之间。")
    else:
        print("成绩不在100到80之间。")

except ValueError:
    # 如果输入的不是整数，打印错误信息
    print("输入错误，请输入一个有效的整数分数。")