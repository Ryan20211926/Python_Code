# coding:utf-8
# @Time    : 2025/5/1 9:02
# @Author  : Ryan
# @FileName: 1. 使用示例.py
"""
"""
import json
import jsonpath
d={
    "error_code":0,
    "stu_info":
    [
        {
            "id":10086,
            "name":"小芳",
            "sex":"女",
            "classname":"三年二班"
        },
        {
            "id": 10000,
            "name": "小龙",
            "sex": "男",
            "classname": "三年三班"
        },
        {
            "id": 10001,
            "name": "小黑",
            "classname": "三年三班"
        }
    ]
}
print(type(d))
name=d["stu_info"][0]["name"]
print(name)
# 模糊匹配 匹配所有学生name
data1=jsonpath.jsonpath(d,"$..name")
print("匹配所有学生name：",data1)
# 精确匹配
# 获取null的值 匹配第一个学生name
data3=jsonpath.jsonpath(d,"$.stu_info[0].name")
print("匹配第一个学生name:",data3)
# 匹配第一个学生name
data4=jsonpath.jsonpath(d,"$.stu_info[0]..name")
print("匹配第一个学生name:",data4)
#匹配前两个学生的信息
data=jsonpath.jsonpath(d,"$.stu_info[:2]")
print("匹配前两个学生的信息：",data)
data5=jsonpath.jsonpath(d,"$.stu_info[?(@.sex=='女')]")
print("匹配性别为女的学生信息:",data5)
data6=jsonpath.jsonpath(d,"$.stu_info[?(@.sex)]")
print("匹配包含性别列的学生信息:",data6)