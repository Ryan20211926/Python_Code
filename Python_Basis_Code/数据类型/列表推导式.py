# coding:utf-8
# @Time    : 2024/12/22 20:18
# @Author  : Ryan
# @FileName: 列表推导式.py

def group_list(input_list, group_size):
    # 使用列表推导式来分组列表中的元素
    return [input_list[i:i + group_size] for i in range(0, len(input_list), group_size)]

# 示例用法
input_list = list(range(1, 101))  # 创建一个包含1到100的列表
group_size = 3  # 设置每个子列表的大小

# 调用函数并打印结果
grouped_list = group_list(input_list, group_size)
for group in grouped_list:
    print(group)