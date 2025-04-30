# coding:utf-8
# @Time    : 2025/4/29 13:21
# @Author  : Ryan
# @FileName: encode函数.py
"""
string.encode(encoding='UTF-8',errors='strict')
参数1：要使用的编码，如"UTF-8、GBK"
参数2：设置不同错误的处理方案。
    默认为 'strict',意为编码错误引起一个UnicodeError。
    其他可能的值有'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'以及通过codecs.register_error() 注册的任何值。
"""
name = '晓达'
v = name.encode(encoding='utf-8',errors='strict')
print(v)
a = name.encode(encoding='gbk',errors='strict')
print(a)
