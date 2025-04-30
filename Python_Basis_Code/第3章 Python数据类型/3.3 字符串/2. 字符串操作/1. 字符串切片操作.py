# coding:utf-8
# @Time    : 2025/4/27 12:51
# @Author  : Ryan
# @FileName: 1. 字符串切片操作.py

# 示例 1：提取子字符串
text = "Hello, World!"
substring = text[0:5]  # 从索引 0 到索引 5（不包含 5）
print(substring)  # 输出：Hello

# 示例 2：省略起始或结束索引
text = "Hello, World!"
substring1 = text[:5]  # 从开头到索引 5（不包含 5）
substring2 = text[7:]  # 从索引 7 到结尾
substring3 = text[:]   # 从开头到结尾（复制整个字符串）
print(substring1)  # 输出：Hello
print(substring2)  # 输出：World!
print(substring3)  # 输出：Hello, World!

# 示例 3：使用负索引
text = "Hello, World!"
substring = text[-6:-1]  # 从倒数第 6 个字符到倒数第 1 个字符（不包含 -1）
print(substring)  # 输出：World

# 示例 4：使用步长
text = "Hello, World!"
substring = text[::2]  # 从开头到结尾，每隔一个字符取一个
print(substring)  # 输出：Hlo ol!

# 示例 5：反转字符串
text = "Hello, World!"
reversed_text = text[::-1]  # 从结尾到开头，步长为 -1
print(reversed_text)  # 输出：!dlroW ,olleH


# 切片操作时，起始偏移量和终止偏移量不在[0,字符串长度-1]这个范围，也不会报错。起始偏移量小于0则会当做0，终止偏移量大于“长度-1”会被当成-1。

# 起始偏移量小于0
s = "Hello, World!"
substring = s[-10:5]
print(substring)  # 输出：Hello

# 终止偏移量大于字符串长度
s = "Hello, World!"
substring = s[0:20]
print(substring)  # 输出：Hello, World!

# 起始偏移量和终止偏移量都不在范围内
s = "Hello, World!"
substring = s[-20:20]
print(substring)  # 输出：Hello, World!