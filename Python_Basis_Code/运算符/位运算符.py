# coding:utf-8
# @Time    : 2024/12/19 13:06
# @Author  : Ryan
# @FileName: 位运算符.py

# 按位与
print(bin(5 & 6))  # 输出: 0b100
# 按位或
print(bin(5 | 6))  # 输出: 0b111
# 按位异或
print(bin(5 ^ 6))  # 输出: 0b011
# 按位非
print(bin(~5))  # 输出: -0b101 (在Python中，按位非操作数通常以补码形式表示)
# 左移位
print(bin(5 << 2))  # 输出: 0b10100
# 右移位
print(bin(20 >> 2))  # 输出: 0b101