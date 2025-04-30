# coding:utf-8
# @Time    : 2025/4/29 13:23
# @Author  : Ryan
# @FileName: format函数.py
"""
"""

# 根据索引位置
tpl = "我是:{0};年龄:{1};性别:{2}"
v = tpl.format("李杰",19,'都行')
print(v)

# 根据变量名
tpl = "我是:{name};年龄:{age};性别:{gender}"
v = tpl.format(name='李杰',age=19,gender='随意')
print(v)

# 根据KV映射关系
tpl = "我是:{name};年龄:{age};性别:{gender}"
v = tpl.format_map({'name':"李杰",'age':19,'gender':'中'})
print(v)
