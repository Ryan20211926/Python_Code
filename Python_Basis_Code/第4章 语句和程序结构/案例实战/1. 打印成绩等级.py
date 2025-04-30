# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:56
# @Author  : Ryan 
# @File    : 1. 打印成绩等级.py
# @Software: PyCharm
"""
# 输入成绩
score = float(input("请输入成绩（0-100分）："))
# 判断成绩等级
if score < 0 or score > 100:
    grade = '无效成绩'
elif 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'E'
# 输出成绩等级
print(f"成绩等级：{grade}")


# 首先判断输入的分数是否在有效范围内（0 到 100 分），如果不在范围内，直接提示用户输入无效。如果有效，再进一步判断成绩等级。
# 输入成绩
score = float(input("请输入成绩（0-100分）："))

# 判断输入的分数是否正确
if 0 <= score <= 100:
    # 成绩有效，进一步判断成绩等级
    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score < 90:
        grade = 'B'
    elif 70 <= score < 80:
        grade = 'C'
    elif 60 <= score < 70:
        grade = 'D'
    else:
        grade = 'E'
    # 输出成绩等级
    print(f"成绩等级：{grade}")
else:
    # 成绩无效
    print("输入的成绩无效，请输入 0 到 100 之间的分数。")