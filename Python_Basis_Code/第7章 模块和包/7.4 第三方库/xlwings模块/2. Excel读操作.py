# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/29 6:48
# @Author  : Ryan 
# @File    : 2. Excel读操作.py
# @Software: PyCharm
"""
"""

# 直接读取工作表中的数据
import xlwings as xw

# 打开一个已存在的 Excel 文件
wb = xw.Book("example.xlsx")  # 替换为你的文件路径

# 选择工作表（可以通过名称或索引选择）
sht = wb.sheets["Sheet1"]  # 按名称选择
# sht = wb.sheets[0]  # 按索引选择（从0开始）

# 读取数据（例如读取 A1:C3 的数据）
data = sht.range("A1:C3").value

# 打印读取的数据
print(data)

# 关闭工作簿
wb.close()

# 将数据读取为 Pandas DataFrame
import xlwings as xw
import pandas as pd

# 打开 Excel 文件
wb = xw.Book("example.xlsx")

# 选择工作表
sht = wb.sheets["Sheet1"]

# 将数据读取为 Pandas DataFrame
df = sht.range("A1:C3").options(pd.DataFrame, header=1, index=False).value

# 打印 DataFrame
print(df)

# 关闭工作簿
wb.close()


# 一次性读取整个工作表
import xlwings as xw

# 打开 Excel 文件
wb = xw.Book("example.xlsx")

# 选择工作表
sht = wb.sheets["Sheet1"]

# 获取工作表的全部数据
data = sht.api.UsedRange.Value

# 打印数据
print(data)

# 关闭工作簿
wb.close()