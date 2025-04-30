# coding:utf-8
# @Time    : 2024/12/21 15:15
# @Author  : Ryan
# @FileName: 指定文件格式上传.py

"""
我可以帮你模拟这个文件上传的过程。请按照以下步骤操作：
1. 键盘输入文件名。
2. 判断文件名长度和扩展名是否满足条件。
3. 根据条件给出相应的提示或生成新的文件名。
现在，请你输入一个文件名，我将进行判断。你可以在这里输入文件名，或者如果你希望我直接进行模拟，
我也可以提供一个示例文件名进行演示。
"""


import random

# 假设用户输入的文件名
file_name = input("请输入文件名：")

# 定义允许的扩展名
allowed_extensions = ('jpg', 'gif', 'png')

import random

def generate_random_string_from_given_chars(given_chars, length):
    random_string = ''
    # 使用for循环生成随机字符串
    for _ in range(length):
        # 使用randint随机选择一个索引，然后从given_chars中选择字符
        random_index = random.randint(0, len(given_chars) - 1)
        random_char = given_chars[random_index]
        random_string += random_char
    return random_string

# 指定的字符串，包含数字和字母
specified_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# 生成一个长度为10的随机字符串
random_str = generate_random_string_from_given_chars(specified_string, 10)
print(random_str)

# 检查文件名长度是否大于6位
if len(file_name) <= 6:
    # 文件名不满足条件
    # 检查扩展名是否满足条件
    if file_name.split('.')[-1] in allowed_extensions:
        # 扩展名满足条件，生成一个6位数字的文件名
        # new_file_name = str(random.randint(100000, 999999)) + "."+file_name.split('.')[-1]
        new_file_name = random_str + "."+file_name.split('.')[-1]
        print(f"成功上传{new_file_name}")
    else:
        # 扩展名不满足条件
        print("上传失败")
else:
    # 文件名满足条件
    # 检查扩展名是否满足条件
    if file_name.split('.')[-1] in allowed_extensions:
        print("上传成功")
    else:
        print("文件格式错误，上传失败")