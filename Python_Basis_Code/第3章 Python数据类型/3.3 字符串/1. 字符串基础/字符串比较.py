# coding:utf-8
# @Time    : 2025/4/27 13:44
# @Author  : Ryan
# @FileName: 字符串比较.py

# 创建三个字符串变量
s1 = 'abc'
s2 = "abc"
s3 = '''
abc
'''

# 打印字符串变量的 id
print("ID of s1:", id(s1))
print("ID of s2:", id(s2))
print("ID of s3:", id(s3))  # 三引号占用的内存空间与单双引号的不同

print("s1 == s2",s1 == s2) # True
print("s1 is s2",s1 is s2) # True

print("s2 == s3",s2 == s3) # False
print("s2 is s3",s2 is s3) # False


s1 = input('请输入：')
s2 = input('请输入：')
print(s1 == s2)
print(s1 is s2)

'''
Python 中值比较（==）和身份比较（is）的区别。值比较检查两个变量的值是否相同，而身份比较检查两个变量是否引用同一个对象。
'''