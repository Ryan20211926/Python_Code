# coding:utf-8
# @Time    : 2024/12/21 14:52
# @Author  : Ryan
# @FileName: 字符串切片.py

# 定义一个字符串
my_string = "Hello, World!"

# 截取从索引1到索引4的字符（包含索引1，不包含索引5）
substring1 = my_string[1:5]
print(substring1)  # 输出: ello

# 截取从索引7到字符串末尾的字符
substring2 = my_string[7:]
print(substring2)  # 输出: World!

# 截取从字符串开头到索引5之前的字符（不包含索引5）
substring3 = my_string[:5]
print(substring3)  # 输出: Hello

# 截取字符串的全部字符
substring4 = my_string[:]
print(substring4)  # 输出: Hello, World!

# 截取字符串的每隔一个字符
substring5 = my_string[::2]
print(substring5)  # 输出: Hlo ol!

# 从后向前截取字符串的每隔一个字符
substring6 = my_string[::-1]
print(substring6)  # 输出: !dlroW ,olleH