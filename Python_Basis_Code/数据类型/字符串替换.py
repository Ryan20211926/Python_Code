# coding:utf-8
# @Time    : 2024/12/21 16:03
# @Author  : Ryan
# @FileName: 字符串替换.py

original_string = "张三和李四是好朋友，他们还有另一个朋友王五。"
# 将“张三”替换为“*”
replaced_string = original_string.replace("张三", "*")

# 将“李四”替换为“*”
replaced_string = replaced_string.replace("李四", "*")

# 如果还有更多的姓名需要替换，可以继续调用replace()
# 将“王五”替换为“*”
replaced_string = replaced_string.replace("王五", "*")

print(replaced_string)  # 输出: *和*是好朋友，他们还有另一个朋友*。

original_string = "张三和李四是好朋友，他们还有另一个朋友王五。"
names_to_replace = ["张三", "李四", "王五"]

# 使用循环替换列表中的所有姓名
for name in names_to_replace:
    original_string = original_string.replace(name, "*")

print(original_string)  # 输出: *和*是好朋友，他们还有另一个朋友*。
