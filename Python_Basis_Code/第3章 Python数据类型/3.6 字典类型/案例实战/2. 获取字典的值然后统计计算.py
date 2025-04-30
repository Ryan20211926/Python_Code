# coding:utf-8
# @Time    : 2025/4/29 12:56
# @Author  : Ryan
# @FileName: 2. 获取字典的值然后统计计算.py
"""
在Python中，要计算字典值的平均值，你需要确保字典中的所有值都是可以相加和除以的数值类型。以下是计算字典值平均值的步骤：
1. 使用 `values()` 方法获取字典中所有的值。
2. 使用 `sum()` 函数计算这些值的总和。
3. 使用 `len()` 函数计算值的数量。
4. 将总和除以数量得到平均值。
"""

# 定义一个字典，其值都是数值类型
my_dict = {'a': 10, 'b': 20, 'c': 30}
# 计算值的总和
total = sum(my_dict.values())
# 计算值的数量
count = len(my_dict)
# 计算平均值
average = total / count if count else 0  # 如果字典为空，则避免除以0的错误
print(f"The average value is: {average}")

# 如果字典中的值不是数值类型，你需要先将它们转换为数值类型，或者过滤掉非数值类型的值。
# 例如，如果字典的值是字符串，你需要确保这些字符串可以被转换为数值
my_dict = {'a': '10', 'b': '20', 'c': '30'}

# 将字符串值转换为整数，并计算平均值
total = sum(int(value) for value in my_dict.values())
count = len(my_dict)

average = total / count if count else 0

print(f"The average value is: {average}")

# 在处理实际数据时，你可能需要添加错误处理机制，以确保在值无法转换为数值时，程序不会崩溃。例如，你可以使用 `try-except` 块来捕获 `ValueError` 异常
my_dict = {'a': '10', 'b': '20', 'c': 'not a number'}

total = 0
count = 0

for value in my_dict.values():
    try:
        total += int(value)
        count += 1
    except ValueError:
        print(f"Value '{value}' is not a number and will be ignored.")

average = total / count if count else 0

print(f"The average value is: {average}")