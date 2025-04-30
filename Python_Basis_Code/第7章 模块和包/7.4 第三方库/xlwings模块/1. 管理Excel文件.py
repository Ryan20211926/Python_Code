# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/29 6:42
# @Author  : Ryan 
# @File    : 1. 管理Excel文件.py
# @Software: PyCharm
"""
"""
import xlwings as xw

# 调用xw库的APP类与Excel建立链接
app = xw.App(visible=True,add_book=False)
# # 创建一个新的工作簿
# wb = xw.Book()
#
# # 获取第一个工作表
# sht = wb.sheets[0]
#
# # 写入数据
# sht.range('A1').value = 'Hello, xlwings!'
#
# # 保存工作簿
# wb.save('example.xlsx')
#
# # 关闭工作簿
# wb.close()