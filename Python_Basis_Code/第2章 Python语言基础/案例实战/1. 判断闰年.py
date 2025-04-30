# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 9:40
# @Author  : Ryan 
# @File    : 1. 判断闰年.py
# @Software: PyCharm
"""

"""
判断闰年的规则如下：
如果年份能被 4 整除，但不能被 100 整除，那么它是闰年。
如果年份能被 100 整除，但不能被 400 整除，那么它不是闰年。
如果年份能被 400 整除，那么它是闰年。
"""
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap_year_input():
    # 输入年份
    year = int(input("请输入一个年份："))
    # 使用 and 和 or 判断闰年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
if __name__ == '__main__':
    # 测试函数
    print(is_leap_year(2020))  # 输出：True
    print(is_leap_year(2021))  # 输出：False
    print(is_leap_year(2000))  # 输出：True
    print(is_leap_year(1900))  # 输出：False
    is_leap_year_input()