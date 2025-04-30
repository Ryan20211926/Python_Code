# coding:utf-8
# @Time    : 2025/4/29 12:53
# @Author  : Ryan
# @FileName: 获取字典所有的key.py
"""
在Python中，要获取字典中的所有键（key）信息，你可以使用字典的 `keys()` 方法。
这个方法会返回一个包含字典中所有键的视图对象。以下是如何使用 `keys()` 方法来获取并遍历字典中的所有键：
"""
# 创建一个字典
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 使用keys()方法获取字典中的所有键
keys = my_dict.keys()
# 遍历并打印所有键
for key in keys:
    print(key)


# 转换为列表 如果你需要对键进行排序或者使用列表方法，可以将 `keys()` 方法返回的视图对象转换为列表
# 将字典中的键转换为列表
keys_list = list(my_dict.keys())
# 打印键的列表
print(keys_list)  # 输出可能是 ['a', 'b', 'c', 'd']，但顺序可能会因Python版本而异


# 直接遍历字典 你也可以直接在 for 循环中遍历字典，这将遍历字典的键
# 直接遍历字典，这将遍历字典的键
for key in my_dict:
    print(key)

