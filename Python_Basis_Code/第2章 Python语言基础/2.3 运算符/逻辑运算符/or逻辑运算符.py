# coding:utf-8
# @Time    : 2025/4/29 13:39
# @Author  : Ryan
# @FileName: or逻辑运算符.py
"""
or 逻辑或 (一真则真，都假才假)

- or 可以对符号两侧的值进行或运算。
- 或运算两个值中只要有一个True，就会返回True。
  如果x为False，返回y的值；如果x为True,不再判断y，返回x的值
  如果两个操作数中至少有一个为True，则结果为True，否则为False。
"""

x = True
y = False
print(x or y)  # 输出：True

# Python中的或运算是短路的或， 或运算是找True的，如果第一个值为True，则不再看第二个值。
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
# 验证or为短路或，找True结束
# 第一个值是True，不会执行print()
True or print('1你猜我出来吗？')
# 第一个值是False，会执行print()
False or print('2你猜我出来吗？')


# 短路 如果x是真直接返回x 如果x是假 直接返回y
print(1 or 1)
print(1 or 2)
print(2 or 1)
print(0 or 1)
print(0 or 2)

# 全0返回0 返回先为真的结果
print(0 or 0 or 0)
print(0 or 1 or 0)
print(0 or 0 or 2)
print(0 or 1 or 2)
print(0 or 2 or 1)