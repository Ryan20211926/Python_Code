# coding:utf-8
# @Time    : 2025/4/29 13:24
# @Author  : Ryan
# @FileName: isalnum函数.py
"""
检测字符串是否由字母和数字、汉字组成
string.isalnum()
如果string至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
"""
name  = 'alex8汉子'
v = name.isalnum()
name1  = 'alex8..*汉子'
v1 = name1.isalnum()
print(v1)
