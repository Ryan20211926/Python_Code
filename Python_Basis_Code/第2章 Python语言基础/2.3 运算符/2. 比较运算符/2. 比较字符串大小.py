# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:35
# @Author  : Ryan 
# @File    : 2. 比较字符串大小.py
# @Software: PyCharm
"""
# 输入三个字符串
str1 = input("请输入第一个字符串：")
str2 = input("请输入第二个字符串：")
str3 = input("请输入第三个字符串：")

# 比较三个字符串的大小
strings = [str1, str2, str3]
strings.sort()  # 使用 sort 方法对字符串列表进行排序

# 输出结果
print("按字典顺序排序后的字符串：")
for s in strings:
    print(s)