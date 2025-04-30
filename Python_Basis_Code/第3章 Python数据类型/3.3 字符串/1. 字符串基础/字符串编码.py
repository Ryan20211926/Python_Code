# coding:utf-8
# @Time    : 2025/4/27 13:15
# @Author  : Ryan
# @FileName: 字符串编码.py


# ord() 函数用于获取字符的 Unicode 编码。它接受一个字符作为参数，并返回该字符的 Unicode 码点（一个整数）。
char = 'A'
unicode_code = ord(char)
print(unicode_code)  # 输出：65

# chr() 函数用于将数字（Unicode 码点）转换回对应的字符。
unicode_code = 65
char = chr(unicode_code)
print(char)  # 输出：A


