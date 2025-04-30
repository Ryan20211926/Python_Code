# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 10:19
# @Author  : Ryan 
# @File    : 3. 模拟加载进度条.py
# @Software: PyCharm
"""
import time

def simulate_progress_bar(total_steps=100, delay=0.1):
    """
    模拟加载进度条
    :param total_steps: 总步数（进度条的总长度）
    :param delay: 每次更新的延迟时间（秒）
    """
    for step in range(total_steps + 1):
        # 计算已完成的百分比
        progress = step / total_steps
        # 格式化输出进度条
        progress_bar = f"[{'#' * step}{'-' * (total_steps - step)}]"
        # 使用 \r 返回行首，覆盖之前的输出
        print('\r加载条：{:<20}|{:>6.1%}'.format(progress_bar,progress),end="")
        # 模拟加载延迟
        time.sleep(delay)

# 调用函数，模拟加载进度条
simulate_progress_bar(total_steps=50, delay=0.1)