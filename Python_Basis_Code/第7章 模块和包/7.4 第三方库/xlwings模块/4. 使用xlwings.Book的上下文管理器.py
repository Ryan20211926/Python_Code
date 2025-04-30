# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/29 6:51
# @Author  : Ryan 
# @File    : 4. 使用xlwings.Book的上下文管理器.py
# @Software: PyCharm
"""
"""

import xlwings as xw

# 使用上下文管理器打开工作簿
with xw.Book("example.xlsx") as wb:
    sht = wb.sheets["Sheet1"]
    data = sht.range("A1:C3").value
    print(data)