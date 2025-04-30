# coding:utf-8
# @Time    : 2025/4/27 13:06
# @Author  : Ryan
# @FileName: 3. 字符串拼接操作.py

"""
在 Python 中，字符串拼接是一种常见的操作，用于将两个或多个字符串合并成一个字符串。
Python 提供了多种方法来实现字符串拼接，
包括使用加号（`+`）操作符、使用 `join()` 方法、使用格式化字符串等。下面是一些常见的字符串拼接方法：
"""


# 1. 使用加号（`+`）操作符 这是最直观的字符串拼接方法，适用于连接少量的字符串。
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # 在两个字符串之间添加空格
print(result)  # 输出：Hello World

# 2. 使用 `join()` 方法 当需要连接列表中的多个字符串时，使用 `join()` 方法更为高效和方便。
words = ["Hello", "World"]
result = " ".join(words)
print(result)  # 输出：Hello World

# 3. 使用格式化字符串（`format()` 方法）这种方法允许你在字符串中嵌入变量，并进行格式化。
name = "World"
result = "Hello, {}!".format(name)
print(result)  # 输出：Hello, World!

# 4. 使用 f-string（Python 3.6+）f-string 是一种新的字符串格式化方法，它使得字符串拼接和变量嵌入更加简洁和高效。
name = "World"
result = f"Hello, {name}!"
print(result)  # 输出：Hello, World!

# 5. 使用 `%` 操作符 这是一种较旧的字符串格式化方法，现在较少使用，但在一些旧代码中仍然可以看到。
name = "World"
result = "Hello, %s!" % name
print(result)  # 输出：Hello, World!



def custom_add(a, b):
    try:
        # 检查两个操作数是否都是字符串
        if isinstance(a, str) and isinstance(b, str):
            return a + b
        # 检查两个操作数是否都是数字
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        # 如果类型不同，则抛出异常
        else:
            raise TypeError("Unsupported operand types for +: '{}' and '{}'".format(type(a).__name__, type(b).__name__))
    except TypeError as e:
        print(e)

# 示例 1：字符串拼接
result1 = custom_add("Hello, ", "World!")
print(result1)  # 输出：Hello, World!

# 示例 2：数字加法
result2 = custom_add(10, 5)
print(result2)  # 输出：15

# 示例 3：类型不同抛出异常
try:
    result3 = custom_add("Hello", 5)
except Exception as e:
    print(e)  # 输出：Unsupported operand types for +: 'str' and 'int'


"""
- **性能**：对于大量字符串的拼接，使用 `join()` 方法通常比使用加号（`+`）操作符更高效，因为后者在每次操作时都会创建新的字符串对象。
- **不可变性**：Python 中的字符串是不可变的，这意味着每次拼接操作都会生成一个新的字符串对象。对于大型字符串或在循环中进行字符串拼接，应考虑使用 `join()` 方法或列表来收集字符串片段，然后一次性拼接。
- **安全性**：当拼接来自用户输入或不可信源的字符串时，应考虑安全性，避免例如 SQL 注入或跨站脚本攻击（XSS）等安全问题。

选择合适的字符串拼接方法可以提高代码的可读性、效率和安全性。
"""
