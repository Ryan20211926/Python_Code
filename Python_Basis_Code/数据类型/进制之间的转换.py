# coding:utf-8
# @Time    : 2024/12/19 12:57
# @Author  : Ryan
# @FileName: 进制之间的转换.py
# 十进制转换为其他进制
decimal_number = 255
binary_string = bin(decimal_number)  # '0b11111111'
octal_string = oct(decimal_number)   # '0o377'
hex_string = hex(decimal_number)     # '0xff'

# 去除前缀，只保留进制表示部分
binary_value = binary_string[2:]  # '11111111'
octal_value = octal_string[2:]    # '377'
hex_value = hex_string[2:]        # 'ff'

# 其他进制转换为十进制
binary_to_decimal = int('11111111', 2)  # 255
octal_to_decimal = int('377', 8)        # 255
hex_to_decimal = int('ff', 16)          # 255

# 使用 format() 函数
formatted_binary = format(11, 'b')      # '1011'
formatted_octal = format(12, 'o')       # '14'
formatted_hex_lower = format(255, 'x')  # 'ff'
formatted_hex_upper = format(255, 'X')  # 'FF'

print(binary_value, octal_value, hex_value)
print(binary_to_decimal, octal_to_decimal, hex_to_decimal)
print(formatted_binary, formatted_octal, formatted_hex_lower, formatted_hex_upper)


