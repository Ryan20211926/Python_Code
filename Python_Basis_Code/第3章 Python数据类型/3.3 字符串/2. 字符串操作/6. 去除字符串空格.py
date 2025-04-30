# coding:utf-8
# @Time    : 2025/4/27 13:18
# @Author  : Ryan
# @FileName: 6. 去除字符串空格.py

# 如果你只想去除字符串两端的空格，可以使用 `strip()` 方法。
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # 输出：Hello, World!

# 如果你只想去除字符串左端或右端的空格，可以使用 `lstrip()` 或 `rstrip()` 方法。
text = "   Hello, World!"
left_stripped = text.lstrip()  # 输出：Hello, World!
right_stripped = text.rstrip() # 输出：   Hello, World!

# 1. 使用 `replace()` 方法 这种方法适用于去除字符串中所有的空格（包括连续的空格）。
text = "Hello, World! This is a test."
no_spaces = text.replace(" ", "")
print(no_spaces)  # 输出：Hello,World!Thisisatest.

# 2. 使用 `split()` 和 `join()` 方法 这种方法同样可以去除字符串中的所有空格，并且可以处理字符串前后的空格。
text = " Hello, World! This is a test. "
no_spaces = ''.join(text.split())
print(no_spaces)  # 输出：Hello,World!Thisisatest.

# 3. 使用列表推导式 这种方法可以去除字符串中的所有空格，并且可以很容易地扩展到去除其他字符。
text = "Hello, World! This is a test."
no_spaces = ''.join([char for char in text if char != ' '])
print(no_spaces)  # 输出：Hello,World!Thisisatest.

# 4. 使用正则表达式 这种方法可以去除字符串中的所有空白字符（包括空格、制表符、换行符等）。
import re
text = " Hello, World! This is a test. "
no_spaces = re.sub(r'\s+', '', text)
print(no_spaces)  # 输出：Hello,World!Thisisatest.

"""
在 Python 中，去除字符串中的空格可以通过多种方法实现，包括使用字符串的 `replace()` 方法、`split()` 和 `join()` 方法组合、列表推导式以及正则表达式等。以下是一些常见的方法：
"""
