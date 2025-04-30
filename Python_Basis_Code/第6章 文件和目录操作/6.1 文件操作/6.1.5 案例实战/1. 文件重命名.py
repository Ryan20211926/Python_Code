# coding:utf-8
# @Time    : 2025/4/28 12:58
# @Author  : Ryan
# @FileName: 1. 文件重命名.py

old_name =input("请输入文件名")

# 2.1 提取文件后缀点的下标
index = old_name.rfind('.')
# 2.2 组织新文件名 旧文件名 + [备份] + 后缀
new_name = old_name[:index] + '备份' + old_name[index:]
print(new_name)
