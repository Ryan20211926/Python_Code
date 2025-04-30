# coding:utf-8
# @Time    : 2025/4/27 13:04
# @Author  : Ryan
# @FileName: join函数.py

# 示例 1：使用空字符串作为连接符
words = ['Hello', 'World', 'Python']
text = ''.join(words)
print(text)  # 输出：HelloWorldPython

# 示例 2：使用空格作为连接符
words = ['Hello', 'World', 'Python']
text = ' '.join(words)
print(text)  # 输出：Hello World Python

# 示例 3：使用逗号和空格作为连接符
words = ['apple', 'banana', 'cherry']
text = ', '.join(words)
print(text)  # 输出：apple, banana, cherry

# 示例 4：使用换行符作为连接符
lines = ["Hello", "World", "Python"]
text = '\n'.join(lines)
print(text)  # 输出：
# Hello
# World
# Python
