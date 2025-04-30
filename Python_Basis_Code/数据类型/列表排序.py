# coding:utf-8
# @Time    : 2024/12/21 21:40
# @Author  : Ryan
# @FileName: 列表排序.py

import random

# 步骤1：生成8个1-100之间的随机整数，保存到列表中
random_numbers = [random.randint(1, 100) for _ in range(8)]
print("生成的随机列表：", random_numbers)

# 步骤2：键盘输入一个1-100之间的整数
try:
    num = int(input("请输入一个1-100之间的整数："))
    if 1 <= num <= 100:
        # 步骤3：将输入的整数插入到排序后的列表中
        random_numbers.append(num)
        random_numbers.sort()  # 升序排序
        # 如果需要降序排序，可以使用 random_numbers.sort(reverse=True)
        print("插入并排序后的列表：", random_numbers)
    else:
        print("输入的数字不在1-100之间，请重新输入。")
except ValueError:
    print("输入的不是整数，请重新输入。")