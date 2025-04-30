# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 20:57
# @Author  : Ryan 
# @File    : 1. 学生投票统计.py
# @Software: PyCharm

# 假设我们有一个学生列表和他们的投票信息，我们将统计每个学生的投票次数。
# 定义一个字典来存储学生的投票信息
votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0,
    "Diana": 0
}

# 模拟学生投票
votes_list = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "Diana", "Charlie", "Bob"]

# 统计每个学生的投票次数
for student in votes_list:
    if student in votes:
        votes[student] += 1
    else:
        votes[student] = 1  # 如果学生不在字典中，添加并初始化为1

# 输出统计结果
print("学生投票统计结果：")
for student, count in votes.items():
    print(f"{student}: {count} 票")