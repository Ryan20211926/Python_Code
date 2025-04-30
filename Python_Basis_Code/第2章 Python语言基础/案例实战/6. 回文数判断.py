# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:41
# @Author  : Ryan 
# @File    : 6. 回文数判断.py
# @Software: PyCharm
"""

"""
回文数是指从左到右和从右到左读都相同的数字。例如，121、12321、123321 等都是回文数
"""

# 将数字转换为字符串
def is_palindrome(num):
    # 将数字转换为字符串，然后检查字符串是否与其反转后的字符串相同。
    # 将数字转换为字符串
    str_num = str(num)
    # 检查字符串是否与其反转后的字符串相同
    return str_num == str_num[::-1]

# 数学方法
def is_palindrome(num):
    # 通过数学运算将数字反转，然后比较原数字和反转后的数字是否相同。
    if num < 0:
        return False  # 负数不是回文数
    original = num
    reversed_num = 0
    while num > 0:
        digit = num % 10  # 取出最后一位数字
        reversed_num = reversed_num * 10 + digit  # 构造反转后的数字
        num //= 10  # 去掉最后一位数字
    return original == reversed_num

# 只反转一半数字
def is_palindrome(num):
    if num < 0 or (num % 10 == 0 and num != 0):
        return False  # 负数或以 0 结尾的非零数字不是回文数
    reversed_half = 0
    while num > reversed_half:
        digit = num % 10
        reversed_half = reversed_half * 10 + digit
        num //= 10
    return num == reversed_half or num == reversed_half // 10

# 递归方法
def is_palindrome(num):
    # 通过递归的方式逐位比较数字的首位和末位。
    def helper(num, reversed_num):
        if num == 0:
            return reversed_num
        digit = num % 10
        return helper(num // 10, reversed_num * 10 + digit)

    if num < 0:
        return False
    return num == helper(num, 0)


# 测试
num = int(input("请输入一个数字："))
if is_palindrome(num):
    print(f"{num} 是回文数")
else:
    print(f"{num} 不是回文数")

if __name__ == '__main__':

    # 测试
    num = int(input("请输入一个数字："))
    if is_palindrome(num):
        print(f"{num} 是回文数")
    else:
        print(f"{num} 不是回文数")

    # 测试
    num = int(input("请输入一个数字："))
    if is_palindrome(num):
        print(f"{num} 是回文数")
    else:
        print(f"{num} 不是回文数")

    num = int(input("请输入一个数字："))
    if is_palindrome(num):
        print(f"{num} 是回文数")
    else:
        print(f"{num} 不是回文数")