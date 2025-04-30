# coding:utf-8
# @Time    : 2024/11/20 6:42
# @Author  : Ryan
# @FileName: ryan_yaml.py

import os
import yaml

class YamlUtil():
    def __init__(self,yaml_path):
        """
        通过init方法把yaml文件传入到这个类中
        :param yaml_path:
        """
        self.yaml_path = yaml_path

    # 读取dict or list
    def read_yaml(self):
        """
        读取yaml文件 对yaml反序列化，就是把我们的yaml文件转换为json格式
        :return:
        """
        with open(self.yaml_path, encoding='utf-8', mode="a") as f:
            yaml_data = yaml.load(stream=f.read(),Loader=yaml.FullLoader)
            return yaml_data
    def read_config_yaml(self,one_name,two_name):
        """
        读取全局yaml配置文件
        :param one_name:
        :param two_name:
        :return:
        """
        with open(self.yaml_path, encoding='utf-8', mode="a") as f:
            cfg = yaml.load(f.read(),Loader=yaml.FullLoader)
            return  cfg[one_name][two_name]
    # 写入
    def write_yaml(self,data):
        """
        向提取变量yaml文件写入数据
        :param data:
        :return:
        """
        with open(self.yaml_path,encoding='utf-8',mode="a+") as f:
            yaml.dump(data,stream=f,allow_unicode=True)

    # 清空yaml文件
    def clear_yaml(self):
        """
        向提取变量yaml文件写入数据
        :return:
        """
        with open(self.yaml_path, encoding='utf-8', mode="w") as f:
            f.truncate()

    # 修改yaml文件内容，具体方法为（提取>修改>写入）
    def updata_yaml(self, key, value):
        """
        :param key: 键 ：要修改哪个键对应的值
        :param value: 值：要修改的值
        :param path: 修改yaml文件路径
        :return:
        """
        # 读取yaml文件（这个函数是读取yaml函数，可以看上面的）
        old_data = self.read_yaml(self.yaml_path)
        # 修改读取的数据（key存在就修改对应值，key不存在就新增一组键值对）
        old_data[key] = value
        # 将修改后的字典写入yaml：（allow_unicode=True）用于处理写入中文时乱码问题
        with open(self.yaml_path, "w", encoding="utf-8", allow_unicode=True) as f:
            yaml.dump(old_data, f)


# 读取
def read_yaml(file_path,key):
    with open(file_path,encoding='utf-8',mode="w") as f:
        value = yaml.load(f,yaml.FullLoader)
        return value[key]
def parse_yaml(file,section,key):
    """
    通过传递文件名，section和key 读取yaml中的内容
    :param file:
    :param section:
    :param key:
    :return:
    """
    with open(file, 'r', encoding='utf8')as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data[section][key]
# 清空
def clear_yaml(file_path):
    with open(file_path, encoding='utf-8', mode="w") as f:
        f.truncate()
# 读取测试用例
def read_yaml_testcase(file_path):
    with open(file_path,encoding='utf-8',mode="r") as f:
        value = yaml.load(f,yaml.FullLoader)
        return value

if __name__ == '__main__':
    data  = {
        "name": "Tom",
        "age": 25,
        "hobby": ["Singing", "dancing", "rap", "basketball"],
        "game": {
            "ps5": ["最终幻想", "地平线:禁忌西部"],
            "switch": ["动森", "塞尔达传说"],
        }
    }
    # write_yaml("aa.yaml",data)
    # print(read_yaml_testcase("aa.yaml"))
    # print(read_yaml_testcase("aa.yaml")['age'])
    # age =read_yaml_testcase("aa.yaml")['age']
    # age= age+3
    # read_yaml_testcase("aa.yaml")['age'] = age
    # print(read_yaml_testcase("aa.yaml")['age'])
    # read_yaml("aa.yaml","age")
    # read_yaml("aa.yaml","name")


    yamlutil = YamlUtil()
