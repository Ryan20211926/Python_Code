# coding:utf-8
# @Time    : 2025/4/27 13:10
# @Author  : Ryan
# @FileName: 4. 字符串格式排版.py

# 1. 使用 `%` 格式化 这是一种较旧的格式化方法，使用 `%` 操作符和元组来替换字符串中的占位符。
name = "Alice"
age = 30
print("Hello, %s. You are %d years old." % (name, age))
# 输出：Hello, Alice. You are 30 years old.

# 2. 使用 `str.format()` 方法 这种方法提供了更多的灵活性，可以使用位置参数或关键字参数来替换占位符。
name = "Bob"
age = 25
print("Hello, {}. You are {} years old.".format(name, age))
# 输出：Hello, Bob. You are 25 years old.
# 使用关键字参数
print("Hello, {name}. You are {age} years old.".format(name="Carol", age=28))
# 输出：Hello, Carol. You are 28 years old.

# 3. 使用 f-string（Python 3.6+） f-string 提供了一种更简洁和直观的方式来嵌入表达式到字符串字面量中。
name = "David"
age = 22
print(f"Hello, {name}. You are {age} years old.")
# 输出：Hello, David. You are 22 years old.


# 4. 对齐和填充 在 `str.format()` 和 f-string 中，可以指定对齐方式和填充字符，以控制字符串的排版。
# 使用 str.format()
print("{:>10}".format("left"))  # 右对齐，总宽度为10
print("{:<10}".format("right")) # 左对齐，总宽度为10
print("{:*^10}".format("center")) # 中心对齐，总宽度为10，用*填充

# 使用 f-string
print(f"{'left':>10}")  # 右对齐，总宽度为10
print(f"{'right':<10}") # 左对齐，总宽度为10
print(f"{'center':*^10}") # 中心对齐，总宽度为10，用*填充

"""
在 Python 中，字符串格式排版通常指的是将字符串中的变量和文本以特定的格式组合在一起。Python 提供了多种方法来实现字符串格式排版，包括传统的 `%` 格式化、`str.format()` 方法、以及 Python 3.6 引入的 f-string（格式化字符串字面量）。以下是这些方法的详细介绍和示例：



### 5. 格式化数字
可以指定数字的格式，如小数点后的位数、千位分隔符等。
```python
# 使用 str.format()
print("{:.2f}".format(3.14159))  # 输出：3.14
print("{:,}".format(1234567))    # 输出：1,234,567

# 使用 f-string
print(f"{3.14159:.2f}")  # 输出：3.14
print(f"{1234567:,}")    # 输出：1,234,567
```

提取的图片内容如下：

```
center()、ljust()、rjust()这三个函数用于对字符串实现排版。
```

以下是 `center()`、`ljust()`、`rjust()` 这三个字符串方法的示例代码：

### 示例 1：使用 `center()` 方法
```python
text = "Hello"
width = 10
centered_text = text.center(width)
print(centered_text)  # 输出：     Hello     
```
在这个例子中，字符串 `"Hello"` 被居中对齐到一个宽度为 10 的字符串中。

### 示例 2：使用 `ljust()` 方法
```python
text = "Hello"
width = 10
left_aligned_text = text.ljust(width)
print(left_aligned_text)  # 输出：Hello      
```
在这个例子中，字符串 `"Hello"` 被左对齐到一个宽度为 10 的字符串中。

### 示例 3：使用 `rjust()` 方法
```python
text = "Hello"
width = 10
right_aligned_text = text.rjust(width)
print(right_aligned_text)  # 输出：      Hello
```
在这个例子中，字符串 `"Hello"` 被右对齐到一个宽度为 10 的字符串中。

### 注意事项
- 这三个方法都接受一个参数 `width`，表示最终字符串的总宽度。
- 如果原字符串的长度大于 `width`，则这些方法不会截断字符串，而是返回原始字符串。
- 这些方法返回一个新的字符串，它们不会修改原始字符串（因为字符串在 Python 中是不可变的）。

### 注意事项

- **可读性**：f-string 提供了最高的可读性，因为它允许直接在字符串中嵌入表达式。
- **性能**：f-string 在性能上通常优于 `%` 格式化和 `str.format()` 方法，特别是在格式化大量字符串时。
- **兼容性**：如果你的代码需要兼容 Python 2.x，那么只能使用 `%` 格式化或 `str.format()` 方法。

选择合适的字符串格式排版方法可以提高代码的可读性和效率，同时确保在不同环境中的兼容性。
"""