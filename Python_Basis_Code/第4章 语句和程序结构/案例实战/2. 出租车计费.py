# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 11:02
# @Author  : Ryan 
# @File    : 2. 出租车计费.py
# @Software: PyCharm
"""

"""
计费规则：
起步价为 2 千米内 5 元。
超过 2 千米后，每增加 1 千米收费 1.5 元。
不足 1 千米的部分按 1 千米计算。
加上燃油附加费 1 元。
"""


def calculate_taxi_fare(distance):
    """
    计算出租车费用
    :param distance: 行驶的距离（千米）
    :return: 总费用
    """
    if distance <= 0:
        return "距离必须大于0千米"

    # 起步价
    base_fare = 5
    base_distance = 2  # 起步距离（千米）
    additional_fare_per_km = 1.5  # 超过起步距离后的每千米费用
    fuel_surcharge = 1  # 燃油附加费

    if distance <= base_distance:
        # 如果距离在起步范围内
        total_fare = base_fare + fuel_surcharge
    else:
        # 超过起步距离的部分
        additional_distance = distance - base_distance
        # 不足1千米按1千米计算
        additional_distance = int(additional_distance) + (1 if additional_distance % 1 != 0 else 0)
        additional_fare = additional_distance * additional_fare_per_km
        total_fare = base_fare + additional_fare + fuel_surcharge

    return total_fare






# 代码优化 列出费用明细
def calculate_taxi_fare_detail(distance):
    """
    计算出租车费用并列出收费明细
    :param distance: 行驶的距离（千米）
    :return: 总费用和收费明细
    """
    if distance <= 0:
        return "距离必须大于0千米", {}

    # 起步价
    base_fare = 5
    base_distance = 2  # 起步距离（千米）
    additional_fare_per_km = 1.5  # 超过起步距离后的每千米费用
    fuel_surcharge = 1  # 燃油附加费

    # 初始化收费明细
    charges = {
        "起步价": base_fare,
        "里程费": 0,
        "燃油附加费": fuel_surcharge
    }

    if distance <= base_distance:
        # 如果距离在起步范围内
        total_fare = base_fare + fuel_surcharge
    else:
        # 超过起步距离的部分
        additional_distance = distance - base_distance
        # 不足1千米按1千米计算
        additional_distance = int(additional_distance) + (1 if additional_distance % 1 != 0 else 0)
        additional_fare = additional_distance * additional_fare_per_km
        charges["里程费"] = additional_fare
        total_fare = base_fare + additional_fare + fuel_surcharge

    charges["总费用"] = total_fare
    return total_fare, charges

if __name__ == '__main__':
    # 输入行驶距离
    distance = float(input("请输入行驶的距离（千米）："))
    # 计算费用
    fare = calculate_taxi_fare(distance)
    # 输出结果
    if isinstance(fare, str):
        print(fare)
    else:
        print(f"总费用：{fare:.2f}元")
    # 计算费用
    fare, charges = calculate_taxi_fare_detail(distance)
    # 输出结果
    if isinstance(fare, str):
        print(fare)
    else:
        print(f"总费用：{fare:.2f}元")
        print("收费明细：")
        for item, cost in charges.items():
            print(f"  {item}: {cost:.2f}元")