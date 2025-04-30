# coding:utf-8
# @Time    : 2024/12/19 6:44
# @Author  : Ryan
# @FileName: 字符串比较.py

# 按字典顺序比较
print("apple" < "banana")  # True，因为'a'在'b'之前
print("apple" > "banana")  # False

# 大小写敏感
print("Apple" < "apple")  # True，大写字母'A'小于小写字母'a'

# 特殊字符
print("zebra" < "Zebra")  # True，因为'z'小于'Z'
print("zebra" < "Zelda")  # True，因为'e'在'l'之前

# 非ASCII字符
print("café" < "cafeé")  # True，因为'é'在'e'之后

# 比较运算符的使用
print("hello" == "hello")  # True，字符串完全相同
print("hello" != "hello")  # False
print("hello" < "hello")  # False
print("hello" > "hello")  # False
print("hello" <= "hello")  # True
print("hello" >= "hello")  # True