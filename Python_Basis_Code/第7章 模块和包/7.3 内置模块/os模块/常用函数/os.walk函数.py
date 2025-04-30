# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/28 6:27
# @Author  : Ryan 
# @File    : os.walk函数.py
# @Software: PyCharm
"""
`os.walk` 是 Python 中 `os` 模块提供的一个非常强大的函数，用于遍历目录树。它可以递归地访问指定目录及其所有子目录中的文件和子目录，并生成一个三元组，包含当前目录路径、当前目录下的子目录列表和当前目录下的文件列表。以下是 `os.walk` 的详细用法：

### 语法
```python
os.walk(top, topdown=True, onerror=None, followlinks=False)
```

### 参数说明
1. **`top`**：指定要遍历的目录的根路径，必须是一个字符串。
2. **`topdown`**（可选，默认为 `True`）：
   - 如果为 `True`，则先遍历指定的目录，再递归遍历其子目录（自上而下）。
   - 如果为 `False`，则先递归遍历子目录，最后遍历指定的目录（自下而上）。
3. **`onerror`**（可选，默认为 `None`）：
   - 如果在访问目录或文件时发生错误，可以通过这个参数指定一个回调函数来处理错误。
   - 回调函数会接收一个异常对象作为参数。如果 `onerror` 为 `None`，则会直接抛出异常。
4. **`followlinks`**（可选，默认为 `False`）：
   - 如果为 `True`，则会跟随符号链接（软链接）进行遍历。
   - 如果为 `False`，则不会遍历符号链接指向的目录或文件。

### 返回值
`os.walk` 返回一个生成器，每次迭代返回一个三元组 `(dirpath, dirnames, filenames)`：
- **`dirpath`**：当前目录的路径（字符串）。
- **`dirnames`**：当前目录下的子目录列表（列表）。
- **`filenames`**：当前目录下的文件列表（列表）。

### 示例代码
以下是一些使用 `os.walk` 的示例代码：

#### 示例 1：基本用法
```python
import os

# 遍历指定目录
for dirpath, dirnames, filenames in os.walk("example_dir"):
    print(f"当前目录路径: {dirpath}")
    print(f"当前目录下的子目录列表: {dirnames}")
    print(f"当前目录下的文件列表: {filenames}")
    print("-" * 40)
```

#### 示例 2：自下而上遍历
```python
import os

# 自下而上遍历目录
for dirpath, dirnames, filenames in os.walk("example_dir", topdown=False):
    print(f"当前目录路径: {dirpath}")
    print(f"当前目录下的子目录列表: {dirnames}")
    print(f"当前目录下的文件列表: {filenames}")
    print("-" * 40)
```

#### 示例 3：处理错误
```python
import os

def handle_error(err):
    print(f"发生错误: {err}")

# 遍历目录并处理错误
for dirpath, dirnames, filenames in os.walk("example_dir", onerror=handle_error):
    print(f"当前目录路径: {dirpath}")
    print(f"当前目录下的子目录列表: {dirnames}")
    print(f"当前目录下的文件列表: {filenames}")
    print("-" * 40)
```

#### 示例 4：跟随符号链接
```python
import os

# 遍历目录并跟随符号链接
for dirpath, dirnames, filenames in os.walk("example_dir", followlinks=True):
    print(f"当前目录路径: {dirpath}")
    print(f"当前目录下的子目录列表: {dirnames}")
    print(f"当前目录下的文件列表: {filenames}")
    print("-" * 40)
```

### 注意事项
1. `os.walk` 不会返回隐藏目录（以 `.` 开头的目录）或隐藏文件（以 `.` 开头的文件），除非它们被明确指定为路径的一部分。
2. 如果目录中包含大量文件和子目录，`os.walk` 的性能可能会受到影响。在这种情况下，可以考虑使用其他方法（如 `os.scandir`）来优化性能。
3. `os.walk` 是一个生成器，每次迭代返回一个目录的信息。如果需要多次使用遍历结果，建议将其结果存储到列表中。

通过 `os.walk`，你可以轻松地遍历目录树并处理文件和目录，非常适合文件系统操作相关的任务，如查找文件、统计文件数量、复制文件等。
"""