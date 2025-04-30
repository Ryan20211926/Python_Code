# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 11:24
# @Author  : Ryan 
# @File    : 5. 小球反弹.py
# @Software: PyCharm
"""

def calculate_bounce(height, bounces):
    """
    计算小球在指定次数落地时的总运行距离和最后一次反弹的高度
    :param height: 初始高度
    :param bounces: 落地次数
    :return: 总运行距离和最后一次反弹的高度
    """
    total_distance = 0  # 总运行距离
    last_bounce_height = height  # 最后一次反弹的高度

    for i in range(bounces):
        # 每次落地后反弹的高度
        bounce_height = last_bounce_height / 2
        # 总运行距离增加：下落距离 + 反弹距离
        total_distance += height + bounce_height
        # 更新初始高度为当前反弹高度
        height = bounce_height
        # 更新最后一次反弹的高度
        last_bounce_height = bounce_height

    return total_distance, last_bounce_height

# 输入初始高度和落地次数
height = 100  # 初始高度为 100 米
bounces = int(input("请输入落地次数："))

# 计算总运行距离和最后一次反弹的高度
total_distance, last_bounce_height = calculate_bounce(height, bounces)

# 输出结果
print(f"小球在 {bounces} 次落地时的总运行距离：{total_distance} 米")
print(f"最后一次反弹的高度：{last_bounce_height} 米")