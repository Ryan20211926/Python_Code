# coding:utf-8
# @Time    : 2025/4/29 13:18
# @Author  : Ryan
# @FileName: center函数.py
"""
在Python中，`center()` 方法是字符串（`str`）对象的一个内置方法，它能够将字符串在指定的宽度内居中显示。如果字符串的长度小于指定的宽度，`center()` 方法会在字符串的左侧和右侧填充指定的字符（默认情况下是空格字符）来达到所需的宽度。

center()方法：返回一个原字符串居中对齐的字符串，并使用指定字符（默认空格）填充至对应长度的新字符串。

### 语法

```python
str.center(width[, fillchar])-> str
```

- `str`：要处理的字符串。
- `width`：指定字符串的总宽度。如果字符串的长度小于这个宽度，那么会在其两侧填充字符来达到这个宽度。如果字符串的长度大于这个宽度，那么字符串将不会被截断，而是保持原样返回。
- `fillchar`（可选）：用于填充的字符。如果省略此参数，则默认使用空格字符 `' '` 来填充。

### 返回值

`center()` 方法返回一个新的字符串，它是原始字符串在指定宽度内居中显示的结果。原始字符串不会被修改（因为Python中的字符串是不可变的）。

### 示例

1. **使用默认填充字符（空格）**

```python
s = "Hello"
centered_s = s.center(10)
print(f"'{centered_s}'")  # 输出: '   Hello   '
```

2. **使用指定的填充字符**

```python
s = "Hello"
centered_s = s.center(10, '*')
print(f"'{centered_s}'")  # 输出: '***Hello***'
```

3. **字符串长度大于指定宽度**

```python
s = "Hello, World!"
centered_s = s.center(5)
print(f"'{centered_s}'")  # 输出: 'Hello, World!'（原样返回）
```

4. **指定宽度为负数**

如果指定的宽度是负数，`center()` 方法将抛出一个 `ValueError` 异常。

```python
s = "Hello"
try:
    centered_s = s.center(-1)
except ValueError as e:
    print(e)  # 输出: center() argument must be non-negative
```

### 注意事项

- `center()` 方法不会改变原始字符串，而是返回一个新的字符串。
- 如果指定的宽度小于或等于字符串的长度，那么字符串将不会被截断或填充，而是保持原样返回。
- 指定的填充字符可以是任何单个字符，包括空格、数字、字母或特殊字符。

通过 `center()` 方法，你可以方便地格式化字符串，使其在输出时具有更好的视觉效果。

文本居中
string.center(width, fillchar=None)
参数1: 表示总长度
参数2：空白处填充的字符（长度为1）
"""
name = 'tong'
v = name.center(20)
print(v)
v = name.center(20,'行')
print(v)


# 字符串序列.center(长度, 填充字符)
# 输出结果：..Pyhton..
mystr = "Pyhton"
new_str = mystr.center(10 , ".")
print(new_str)

"""
 有的时候可能不是绝对居中， 补充字符数可能是奇数， 调整长度即可让补充字符数变成偶数， 来达到绝对居中效果。
"""
s1 = 'abc'
print(s1.center(50,'#'))