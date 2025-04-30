# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 9:43
# @Author  : Ryan 
# @File    : 2. 计算圆的周长面积体积.py
# @Software: PyCharm
"""
import math

# 输入圆的半径和圆柱的高
radius = float(input("请输入圆的半径："))
height = float(input("请输入圆柱的高："))

# 计算圆的周长
circumference = 2 * math.pi * radius

# 计算圆的面积
area_circle = math.pi * radius ** 2

# 计算圆柱的表面积
# 圆柱的表面积 = 2 * 圆的面积 + 圆柱的侧面积
# 圆柱的侧面积 = 圆的周长 * 高
side_area = circumference * height
surface_area_cylinder = 2 * area_circle + side_area

# 计算圆柱的体积
volume_cylinder = area_circle * height

# 计算球的体积
volume_sphere = (4 / 3) * math.pi * (radius ** 3)

# 输出结果
print(f"圆的周长：{circumference:.2f}")
print(f"圆的面积：{area_circle:.2f}")
print(f"圆柱的表面积：{surface_area_cylinder:.2f}")
print(f"圆柱的体积：{volume_cylinder:.2f}")
print(f"球的体积：{volume_sphere:.2f}")