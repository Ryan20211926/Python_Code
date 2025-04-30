# coding:utf-8
# @Time    : 2024/12/1 22:00
# @Author  : Ryan
# @FileName: ryan_opera_yaml.py
from commons.ryan_help import *
import yaml

class OperaYaml:
    def readYaml(self):
        with open(FilePath('data','data.yaml'),encoding='utf-8') as fp:
            return list(yaml.safe_load_all(fp))
    def readBookYaml(self):
        with open(FilePath(filePath='data',fileName='book.yaml'),encoding='utf-8') as fp:
            return yaml.safe_load(fp)
if __name__ == '__main__':
    obj = OperaYaml()
    # print(type(obj.readBookYaml()['book_002']))
    # for item in obj.readYaml():
    #     print(item)