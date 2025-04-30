# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 11:21
# @Author  : Ryan 
# @File    : 3. 水仙花数.py
# @Software: PyCharm
"""

"""
水仙花数（Narcissistic Number），又称阿姆斯特朗数（Armstrong Number），
是指一个三位数，其各位数字的立方和等于该数本身。例如：153 = 1³ + 5³ + 3³。
"""
def is_narcissistic_number(num):
    """
    判断一个数字是否是水仙花数
    :param num: 输入的数字
    :return: 是否是水仙花数
    """
    # 将数字转换为字符串，以便逐位处理
    num_str = str(num)
    # 检查是否为三位数
    if len(num_str) != 3:
        return False
    # 计算各位数字的立方和
    sum_of_cubes = sum(int(digit) ** 3 for digit in num_str)
    # 判断立方和是否等于原数
    return sum_of_cubes == num

# 输入数字
try:
    num = int(input("请输入一个三位数："))
    # 判断是否是水仙花数
    if is_narcissistic_number(num):
        print(f"{num} 是水仙花数")
    else:
        print(f"{num} 不是水仙花数")
except ValueError:
    print("输入无效，请输入一个整数。")