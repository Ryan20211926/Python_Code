# coding:utf-8
# @Time    : 2025/4/29 13:24
# @Author  : Ryan
# @FileName: isalpha函数.py
"""
检测字符串是否只由字母组成
string.isalpha()
如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
"""
name  = 'alex'
name1  = 'alex8..*汉子'
v1 = name.isalpha()
print(v1)
v2 = name1.isalpha()
print(v2)
