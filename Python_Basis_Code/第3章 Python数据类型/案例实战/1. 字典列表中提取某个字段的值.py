# coding:utf-8
# @Time    : 2025/5/7 12:46
# @Author  : Ryan
# @FileName: 1. 字典列表中提取某个字段的值.py

# 假设你有一个字典列表，每个字典都包含一个名为 `key` 的字段，你想提取所有字典中 `key` 的值：
# 示例字典列表
dict_list = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

# 提取字段值
field_name = "name"  # 想要提取的字段名
extracted_values = [d[field_name] for d in dict_list if field_name in d]
print(extracted_values)
extracted_values = [(d.get("name", "无名氏"), d.get("age", 0)) for d in dict_list]
print(extracted_values)
# 假设字典中包含嵌套结构：
dict_list = [
    {"name": "Alice", "details": {"age": 25, "city": "New York"}},
    {"name": "Bob", "details": {"age": 30, "city": "Los Angeles"}},
    {"name": "Charlie", "details": {"age": 35, "city": "Chicago"}}
]
extracted_values = [d["details"]["age"] for d in dict_list if "details" in d and "age" in d["details"]]
print(extracted_values)
def extract_field_from_dicts(dict_list, field_name, default=None):
    """
    从字典列表中提取指定字段的值，并返回一个列表。

    :param dict_list: 包含字典的列表
    :param field_name: 要提取的字段名
    :param default: 如果字段不存在时的默认值（可选）
    :return: 包含提取值的列表
    """
    return [d.get(field_name, default) for d in dict_list]
dict_list = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

# 提取字段 "name"
extracted_names = extract_field_from_dicts(dict_list, "name")
print(extracted_names)

#### 示例 2：提取字段并提供默认值
# 提取字段 "city"，如果不存在则返回 "Unknown"
extracted_cities = extract_field_from_dicts(dict_list, "city", default="Unknown")
print(extracted_cities)
# 示例 3：提取嵌套字段 如果需要提取嵌套字段，可以稍微修改函数以支持嵌套路径
def extract_nested_field_from_dicts(dict_list, field_path, default=None):
    """
    从字典列表中提取嵌套字段的值，并返回一个列表。

    :param dict_list: 包含字典的列表
    :param field_path: 嵌套字段的路径，以点分隔（例如 "details.age"）
    :param default: 如果字段不存在时的默认值（可选）
    :return: 包含提取值的列表
    """
    def get_nested_value(d, path):
        """递归获取嵌套字段的值"""
        fields = path.split(".")
        for field in fields:
            if isinstance(d, dict) and field in d:
                d = d[field]
            else:
                return default
        return d

    return [get_nested_value(d, field_path) for d in dict_list]

#### 使用示例：提取嵌套字段
dict_list = [
    {"name": "Alice", "details": {"age": 25, "city": "New York"}},
    {"name": "Bob", "details": {"age": 30, "city": "Los Angeles"}},
    {"name": "Charlie", "details": {"age": 35, "city": "Chicago"}}
]

# 提取嵌套字段 "details.age"
extracted_ages = extract_nested_field_from_dicts(dict_list, "details.age")
print(extracted_ages)
