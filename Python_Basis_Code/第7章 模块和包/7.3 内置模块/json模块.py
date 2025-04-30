# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/22 21:43
# @Author  : Ryan 
# @File    : json模块.py
# @Software: PyCharm
"""
import json


def parse_json(file,key1,key2):
    '''
    封装一下解析json的函数，支持两层的json文件,两个key
    '''
    mylist = []
    with open(file,'r',encoding='utf8') as f:
        data = json.load(f)
    for i in data:
        mylist.append((data[i][key1],data[i][key2]))
    return mylist

if __name__ == '__main__':
    account_info = parse_json('login_account.json', 'name', 'password')
    print(account_info)