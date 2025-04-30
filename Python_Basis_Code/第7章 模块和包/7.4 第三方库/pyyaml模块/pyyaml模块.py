# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/22 21:48
# @Author  : Ryan 
# @File    : pyyaml模块.py
# @Software: PyCharm
"""
import yaml
def parse_yml(file, section, key):
    '''
    通过传递文件名，section和key，取yml文件中的内容
    '''
    with open(file, 'r', encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data[section][key]


if __name__ == '__main__':
    value = parse_yml('my_yaml_3.yml', 'websites', 'URL')
    print(value)