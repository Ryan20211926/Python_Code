# coding:utf-8
# @Time    : 2025/4/28 12:28
# @Author  : Ryan
# @FileName: 1. 三元表达式.py

x = 10
y = 20
max_value = x if x > y else y
print(max_value)  # 输出 20

name = "Alice"
greeting = "Hello, " + name + "!" if name else "Hello, stranger!"
print(greeting)  # 输出 "Hello, Alice!"

# 在函数中使用

def get_absolute_value(x):
    return x if x >= 0 else -x

print(get_absolute_value(-5))  # 输出 5
print(get_absolute_value(10))  # 输出 10

a = 1
b = 2
c = 3
result = a if a > b else (b if b > c else c)
print(result)
