# coding:utf-8
# @Time    : 2024/12/19 6:48
# @Author  : Ryan
# @FileName: 逻辑运算符.py


# 逻辑与
print(True and True)  # 输出 True
print(True and False)  # 输出 False

# 逻辑或
print(False or True)  # 输出 True
print(False or False)  # 输出 False

# 逻辑非
print(not True)  # 输出 False
print(not False)  # 输出 True

# 组合使用逻辑运算符
print(True and (False or True))  # True，因为(False or True) 结果为 True，然后 True and True 结果为 True
print(not (True and False))  # True，因为(True and False) 结果为 False，然后 not False 结果为 True

print(0 and 11)

# 逻辑与
print("" and "Hello")  # 输出 ""
print("World" and "Hello")  # 输出 "Hello"

# 逻辑或
print("Hello" or "World")  # 输出 "Hello"
print("" or "World")  # 输出 "World"

# 逻辑非
print(not "")  # 输出 True
print(not "Hello")  # 输出 False

# 组合使用逻辑运算符
print(not ("" or "This will not be printed")) # True，因为 ("" or "This will not be printed") 结果为 "This will not be printed"，然后 not "This will not be printed" 结果为 False
print("" and ("Hello" or "World"))  # ""，因为 ("Hello" or "World") 结果为 "Hello"，然后 "" and "Hello" 结果为 ""