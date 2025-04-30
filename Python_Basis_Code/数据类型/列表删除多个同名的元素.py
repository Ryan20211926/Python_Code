# coding:utf-8
# @Time    : 2024/12/21 21:10
# @Author  : Ryan
# @FileName: 列表删除多个同名的元素.py

my_list = ['apple', 'banana', 'cherry', 'apple', 'date', 'banana']
# 要删除的元素
element_to_remove = 'apple'
# 从后向前遍历列表，删除所有同名的元素
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == element_to_remove:
        del my_list[i]
print(my_list)  # 输出: ['banana', 'cherry', 'date', 'banana']