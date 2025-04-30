# coding:utf-8
# @Time    : 2025/4/27 13:55
# @Author  : Ryan
# @FileName: 1. 根据输入年龄输出不同信息.py

age = int(input('请猜猜宋宋姐年龄：'))
if age <= 18 and age > 0:
    print('(oﾟ▽ﾟ)o☆[BINGO!] 太有眼光啦！')
elif age > 18 and age <= 30:
    print('人家还是宝宝呢……')
elif age > 30 and age <= 40:
    print('长得太年轻了吧!!!!!')
else:
    print('输入错误！')