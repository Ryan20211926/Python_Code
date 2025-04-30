# coding:utf-8
# @Time    : 2024/12/21 0:52
# @Author  : Ryan
# @FileName: 打印图形.py
print('-----打印星号三角形-----')

rows = 5
for i in range(1, rows + 1):
    print('* ' * i)
print('-----打印星号矩形-------')
rows = 3
cols = 5
for _ in range(rows):
    print('* ' * cols)
print('---------打印正方形星号图案--------')
# 定义正方形的边长
size = 5
# 外层循环控制行数
row = 0
while row < size:
    # 内层循环控制每行的星号数量
    col = 0
    while col < size:
        print('*', end='')  # 不换行打印星号
        col += 1
    print()  # 内层循环结束后换行
    row += 1
print('-----------打印直角三角形星号图案-----------------')
# 定义三角形的高度
height = 5
# 外层循环控制行数
row = 1
while row <= height:
    # 内层循环控制每行的星号数量
    col = 1
    while col <= row:
        print('*', end='')  # 不换行打印星号
        col += 1
    print()  # 内层循环结束后换行
    row += 1
print('------------打印倒置直角三角形星号图案----------------')
# 定义三角形的高度
height = 5

# 外层循环控制行数
row = height
while row > 0:
    # 内层循环控制每行的星号数量
    col = 1
    while col <= row:
        print('*', end='')  # 不换行打印星号
        col += 1
    print()  # 内层循环结束后换行
    row -= 1
print('----------------------------')