# coding:utf-8
# @Time    : 2025/4/29 13:38
# @Author  : Ryan
# @FileName: and逻辑运算符.py
"""
and 逻辑与 （一假则假，都真才真）
- and可以对符号两侧的值进行与运算。
- 只有在符号两侧的值都为True时，才会返回True，只要有一个False就返回False
  and与运算 如果x为False，x and y返回False，如果x为True,返回y的计算值。本质是，z=True and y =y,如果x是真的话，最终结果取决于y
"""
#如果x为False，x and y返回False；
print(0 and 2) # 0
# 如果x为True,返回y的计算值。
print(1 and 2) # 2
print(1 and 99) # 99
print(-1 and 99) #99


# Python中的与运算是短路的与，也就是说与运算是找False的，如果第一个值为False，则不再看第二个表达式的结果。
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
# 验证and为短路与，找False结束
# 第一个值是True，会执行print()
True and print('1你猜我出来吗？')
# 第一个值是False，不会执行print()
False and print('2你猜我出来吗？')
