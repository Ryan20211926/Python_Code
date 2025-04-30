# coding:utf-8
# @Time    : 2024/12/22 8:43
# @Author  : Ryan
# @FileName: 字典遍历.py

# 创建一个字典
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 使用items()方法获取字典中的所有键值对
items = my_dict.items()
print(items) # dict_items([('a', 1), ('b', 2), ('c', 3)])
# 遍历并打印所有键值对
for key, value in items:
    print(f"{key}: {value}")
# 遍历并打印所有键值对元组
for item in items:
    print(f"{item}")