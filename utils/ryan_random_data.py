# coding:utf-8
# @Time    : 2025/4/27 12:40
# @Author  : Ryan
# @FileName: ryan_random_data.py

from utils.ryan_log import ApiAutoLog
loger = ApiAutoLog()

import random
import string

def generate_six_digit_random_number():
    """
    生成一个 6 位的随机数。
    返回值：一个 6 位的整数。
    """
    result = random.randint(100000, 999999)
    loger.info(f"6位数字随机数：{result}")
    return result




def generate_captcha(length=6):
    """
    生成指定长度的验证码。
    参数：
    - length: 验证码的长度，默认为 6 位。
    返回值：
    - 一个由字母和数字组成的随机字符串。
    """
    # 定义验证码的字符池（包括大小写字母和数字）
    characters = string.ascii_letters + string.digits+string.punctuation
    # 定义验证码的字符池（包括大小写字母和数字和标点符号）
    characters = string.ascii_letters + string.digits+string.punctuation
    # 使用 random.choices 随机选择字符
    captcha = ''.join(random.choices(characters, k=length))
    loger.info(f"长度{length}的验证码:{captcha}")
    return captcha


def select_random_element(input_list):
    """
    从给定的列表中随机选择一个元素。
    参数: input_list (list): 要从中选择元素的列表。
    返回:object: 随机选中的元素。
    """
    if not input_list:  # 检查列表是否为空
        raise ValueError("列表不能为空")
    result = random.choice(input_list)
    loger.info(f"从列表{input_list}中选取的元素:{result}")
    return result

import random

def select_multiple_elements(input_list, num_elements):
    """
    从给定的列表中随机选择多个元素，并返回一个新的列表。
    参数:
        input_list (list): 要从中选择元素的列表。
        num_elements (int): 要选择的元素数量。
    返回:list: 随机选中的元素组成的新列表。
    异常:
        ValueError: 如果列表为空，或者要选择的元素数量超过列表长度。
    """
    if not input_list:
        raise ValueError("列表不能为空")
    if num_elements > len(input_list):
        raise ValueError("要选择的元素数量不能超过列表的长度")
    if num_elements <= 0:
        raise ValueError("要选择的元素数量必须大于0")
    result = random.sample(input_list, num_elements)
    loger.info(f"从列表{input_list}中选择的{num_elements}个元素返回的值:{result}")
    return result

def get_specified_length_hanzi(length):
    hanzi_list = []
    # 遍历Unicode范围
    for code in range(0x4e00, 0x9fff + 1):
        char = chr(code)  # 将Unicode编码转换为字符
        hanzi_list.append(char)  # 将汉字添加到列表中
    else:
        result = "".join(select_multiple_elements(hanzi_list,length))
        loger.info(f"选取的{length}个汉字:{result}")



def get_list_to_str(list_to_str):
    # 将所有元素转换为字符串
    string_data = [str(item) for item in list_to_str]
    # 使用 "".join() 拼接成一个字符串
    result = "".join(string_data)
    loger.info(f"{list_to_str}转换为字符串{result}")
    return result


if __name__ == '__main__':
    loger.info(f"")
    loger.info(f"{__file__}")
    generate_six_digit_random_number()
    generate_captcha()
    input_list = [1,2,3,4,5]
    select_random_element(input_list)
    select_multiple_elements(input_list,3)
    get_specified_length_hanzi(20)
    input_list = [1, 2, 3, "a", "b", 4]
    get_list_to_str(input_list)

