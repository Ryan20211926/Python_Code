# coding:utf-8
# @Time    : 2024/12/18 22:03
# @Author  : Ryan
# @FileName: 打印个位数十位数百位数.py

# 获取用户输入的三位数
number = input("请输入一个三位数：")

# 确保输入的是三位数
if len(number) == 3 and number.isdigit():
    # 分离出百位、十位和个位
    hundreds = number[0]
    tens = number[1]
    units = number[2]
    # 打印结果
    print(f"百位数是：{hundreds}")
    print(f"十位数是：{tens}")
    print(f"个位数是：{units}")
else:
    print("输入的不是三位数，请重新输入。")

# 提示用户输入一个三位数
num = input("请输入一个三位数: ")

# 检查输入是否为三位数且为数字
if len(num) == 3 and num.isdigit():
    # 将输入转换为整数
    number = int(num)

    # 计算个位数、十位数和百位数
    ones = number % 10  # 个位数
    tens = (number // 10) % 10  # 十位数
    hundreds = number // 100  # 百位数

    # 打印结果
    print("个位数是:", ones)
    print("十位数是:", tens)
    print("百位数是:", hundreds)
else:
    print("输入无效，请输入一个三位数。")