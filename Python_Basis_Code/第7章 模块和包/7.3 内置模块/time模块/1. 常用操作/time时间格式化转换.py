# coding:utf-8
# @Time    : 2024/12/3 21:43
# @Author  : Ryan
# @FileName: time时间格式化转换.py
import time
localtime = time.asctime(time.localtime())
print ("本地时间为 :", localtime)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
