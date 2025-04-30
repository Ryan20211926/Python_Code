# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/20 21:17
# @Author  : Ryan 
# @File    : ryan_time.py
# @Software: PyCharm
"""

import datetime
import time
from utils.ryan_log import ApiAutoLog
loger = ApiAutoLog()

def get_time_by_datetime(format_string="%Y-%m-%d %H:%M:%S"):
    # 获取当前时间
    now = datetime.datetime.now()
    # 2.6 格式化输出
    formatted_time = now.strftime(format_string)
    loger.info(f"格式化后的当前时间：{formatted_time}")
    return formatted_time


def get_time_by_time(format_string="%Y-%m-%d %H:%M:%S"):
    """
    根据传入的格式化字符串返回当前时间的格式化结果。
    :param format_string: 时间格式化字符串，例如 "%Y-%m-%d %H:%M:%S"
    :return: 格式化后的当前时间字符串
    """
    # 获取当前时间的时间戳
    current_time = time.time()
    # 将时间戳转换为本地时间的 struct_time 对象
    local_time = time.localtime(current_time)
    # 根据格式化字符串格式化时间
    formatted_time = time.strftime(format_string, local_time)
    loger.info(f"格式化后的当前时间：{formatted_time}")
    return formatted_time

def get_today_by_datetime():
    today_date = datetime.date.today()
    loger.info(f"今天日期是：{today_date}")
    return today_date

def get_today_by_datetime_format(format="%Y-%m-%d"):
    today_date = datetime.date.today()
    formatted_date = today_date.strftime(format)
    loger.info(f"{format}格式化后的时间是：{today_date}")
    return formatted_date

def get_day_of_week_by_datetime():
    today_date = datetime.date.today()
    # %A 返回完整的星期几名称（如 Monday、Tuesday 等）
    # day_of_week = today_date.strftime("%A")
    # 如果需要返回星期几的数字（0 表示星期一，6 表示星期日），可以使用 weekday()
    day_of_week = today_date.weekday() # 0（表示星期一）
    loger.info(f"今天的日期是：{today_date} 是星期{day_of_week}")
    # print(day_of_week)  # 输出：Monday

def get_yesterday_by_datetime_format(format="%Y-%m-%d",**kwargs):
    current_datetime = datetime.datetime.now()
    # 根据key获取时间
    past_datetime = current_datetime - datetime.timedelta(**kwargs)
    formatted_date = past_datetime.strftime(format)
    if "days" in kwargs:
        loger.info(f"当前时间:{current_datetime}，过去{kwargs.get('days')}天的时间:{formatted_date}")
    elif "hours" in kwargs:
        loger.info(f"当前时间:{current_datetime}，过去{kwargs.get('hours')}小时的时间:{formatted_date}")
    elif "seconds" in kwargs:
        loger.info(f"当前时间:{current_datetime}，过去{kwargs.get('seconds')}秒的时间:{formatted_date}")


def convert_seconds(total_seconds):
    # 计算天数
    days, remaining_seconds = divmod(total_seconds, 86400)
    # 计算小时数
    hours, remaining_seconds = divmod(remaining_seconds, 3600)
    # 计算分钟数
    minutes, remaining_seconds = divmod(remaining_seconds, 60)
    # 剩下的秒数就是最终的秒数
    seconds = remaining_seconds
    loger.info(f"耗费时间{days}天{hours}小时{minutes}分{seconds}秒")
    return days, hours, minutes, seconds



if __name__ == '__main__':
    loger.info(f"")
    loger.info(f"{__file__}")
    get_time_by_datetime()
    get_time_by_time()
    get_today_by_datetime()
    get_today_by_datetime_format()
    get_day_of_week_by_datetime()
    get_yesterday_by_datetime_format()
    get_yesterday_by_datetime_format(days=7)
    get_yesterday_by_datetime_format(hours=7)
    get_yesterday_by_datetime_format(seconds=7)
    get_yesterday_by_datetime_format(format="%Y-%m-%d %H:%M:%S",days=10)
    total_seconds = 12345
    convert_seconds(total_seconds)