# coding:utf-8
# @Time    : 2025/4/27 13:52
# @Author  : Ryan
# @FileName: 2. 生成随机数.py

s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm9987654321'
print(len(s))  # 求字符串长度 len(str),返回值是一个整型的数值
# 四个随机数
code = ''

import random

# IndexError: string index out of range  s = 'abc'  print(s[3])
# index: 0~len(s)-1  0~61
for i in range(4):
    ran = random.randint(0,len(s)-1)
    print(ran)
    code += s[ran]
else:
    print(code)