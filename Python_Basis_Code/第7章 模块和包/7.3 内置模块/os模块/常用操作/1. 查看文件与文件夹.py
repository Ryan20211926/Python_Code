# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 22:08
# @Author  : Ryan 
# @File    : 1. 查看文件与文件夹.py
# @Software: PyCharm


# 1. 使用 os.listdir() 函数可以列出指定目录下的所有文件和文件夹名称，但不会区分文件和文件夹。
import os
# 指定目录路径
directory_path = "your_directory_path"
# 获取目录中的所有文件和文件夹名称
entries = os.listdir(directory_path)
for entry in entries:
    print(entry)
"""
在 Python 中，`os` 模块提供了丰富的功能来操作文件系统，包括查看目录中的文件和文件夹。以下是几种常用的方法来查看指定目录中的所有文件和文件夹。

### 2. **使用 `os.scandir()`**
`os.scandir()` 函数返回一个迭代器，可以获取目录中的文件和文件夹的详细信息（如文件类型、大小等）。它比 `os.listdir()` 更高效，因为它返回的是 `os.DirEntry` 对象。

#### 示例代码
```python
import os

# 指定目录路径
directory_path = "your_directory_path"

# 使用 os.scandir() 遍历目录
with os.scandir(directory_path) as entries:
    for entry in entries:
        if entry.is_file():
            print(f"File: {entry.name}")
        elif entry.is_dir():
            print(f"Directory: {entry.name}")
```

### 3. **使用 `os.walk()`**
`os.walk()` 是一个更强大的工具，它可以递归地遍历目录树，返回每个目录的路径、子目录列表和文件列表。它非常适合用于深度遍历目录结构。

#### 示例代码
```python
import os

# 指定目录路径
directory_path = "your_directory_path"

# 使用 os.walk() 遍历目录树
for root, dirs, files in os.walk(directory_path):
    print(f"Current Directory: {root}")
    print("Subdirectories:")
    for dir in dirs:
        print(f"  Directory: {dir}")
    print("Files:")
    for file in files:
        print(f"  File: {file}")
    print()
```

### 4. **使用 `pathlib` 模块**
`pathlib` 是 Python 3.4 引入的现代文件系统路径操作模块，它提供了面向对象的方式来处理文件和目录。`pathlib` 提供了更简洁和直观的 API。

#### 示例代码
```python
from pathlib import Path

# 指定目录路径
directory_path = Path("your_directory_path")

# 获取目录中的所有文件和文件夹
entries = directory_path.iterdir()

for entry in entries:
    if entry.is_file():
        print(f"File: {entry.name}")
    elif entry.is_dir():
        print(f"Directory: {entry.name}")
```

### 5. **递归遍历目录（`pathlib` 版本）**
如果需要递归遍历目录，`pathlib` 也提供了类似 `os.walk()` 的功能。

#### 示例代码
```python
from pathlib import Path

# 指定目录路径
directory_path = Path("your_directory_path")

# 递归遍历目录
for entry in directory_path.rglob("*"):
    if entry.is_file():
        print(f"File: {entry}")
    elif entry.is_dir():
        print(f"Directory: {entry}")
```

### 6. **比较 `os` 和 `pathlib`**
- **`os` 模块**：
  - 更传统，适合 Python 2 和 Python 3。
  - 提供了丰富的底层文件系统操作功能。
  - 需要手动拼接路径字符串。
- **`pathlib` 模块**：
  - 更现代，面向对象，代码更简洁。
  - 提供了更高级的路径操作功能。
  - 自动处理路径分隔符等问题。

### 总结
- 如果需要快速列出目录中的文件和文件夹，可以使用 `os.listdir()` 或 `os.scandir()`。
- 如果需要递归遍历目录树，推荐使用 `os.walk()` 或 `pathlib.Path.rglob()`。
- 如果你更喜欢面向对象的编程方式，推荐使用 `pathlib` 模块。

根据你的具体需求选择合适的方法即可！
"""
