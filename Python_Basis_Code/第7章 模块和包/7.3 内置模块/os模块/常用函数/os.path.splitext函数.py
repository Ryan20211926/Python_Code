# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 22:19
# @Author  : Ryan 
# @File    : os.path.splitext函数.py
# @Software: PyCharm
"""
`os.path.splitext()` 是 Python 的 `os.path` 模块中的一个函数，用于将文件名分割成文件名和扩展名两部分。它在处理文件路径时非常有用，尤其是在需要分离文件名和扩展名的场景中。

### 函数语法
```python
os.path.splitext(path)
```

- **参数**：
  - `path`：需要分割的文件路径（可以是相对路径或绝对路径）。
- **返回值**：
  - 返回一个元组 `(root, ext)`：
    - `root`：文件名部分（不包括扩展名）。
    - `ext`：扩展名部分（包括点号 `.`，如果没有扩展名则为空字符串）。

### 示例
#### 示例 1：分割带有扩展名的文件路径
```python
import os

file_path = "example.txt"
root, ext = os.path.splitext(file_path)

print("File name:", root)  # 输出：File name: example
print("Extension:", ext)   # 输出：Extension: .txt
```

#### 示例 2：分割没有扩展名的文件路径
```python
import os

file_path = "example"
root, ext = os.path.splitext(file_path)

print("File name:", root)  # 输出：File name: example
print("Extension:", ext)   # 输出：Extension: (空字符串)
```

#### 示例 3：分割包含目录路径的文件路径
```python
import os

file_path = "/path/to/example.txt"
root, ext = os.path.splitext(file_path)

print("File name:", root)  # 输出：File name: /path/to/example
print("Extension:", ext)   # 输出：Extension: .txt
```

### 注意事项
1. **扩展名的定义**：
   - `os.path.splitext()` 将最后一个点号（`.`）及其后面的内容视为扩展名。如果文件名中有多个点号，只有最后一个点号及其后面的内容会被视为扩展名。
   - 例如：
     ```python
     file_path = "example.tar.gz"
     root, ext = os.path.splitext(file_path)
     print(root)  # 输出：example.tar
     print(ext)   # 输出：.gz
     ```

2. **特殊情况**：
   - 如果文件名以点号开头（例如隐藏文件），`os.path.splitext()` 会将整个文件名视为扩展名。
     ```python
     file_path = ".hiddenfile"
     root, ext = os.path.splitext(file_path)
     print(root)  # 输出：（空字符串）
     print(ext)   # 输出：.hiddenfile
     ```

3. **路径分隔符**：
   - `os.path.splitext()` 会正确处理路径分隔符（`/` 或 `\`），因此可以安全地用于包含目录路径的文件路径。

### 使用场景
`os.path.splitext()` 常用于以下场景：
- **文件处理**：在处理文件时，根据扩展名判断文件类型（例如，区分文本文件、图片文件等）。
- **文件重命名**：在重命名文件时，保留原始扩展名。
- **文件过滤**：根据扩展名过滤特定类型的文件。

### 示例：过滤特定扩展名的文件
假设我们需要列出某个目录下所有 `.txt` 文件：
```python
import os

directory_path = "/path/to/directory"
txt_files = []

for filename in os.listdir(directory_path):
    root, ext = os.path.splitext(filename)
    if ext == ".txt":
        txt_files.append(filename)

print("Text files:", txt_files)
```

### 总结
`os.path.splitext()` 是一个非常实用的函数，能够方便地将文件路径分割成文件名和扩展名两部分。它在处理文件路径时非常方便，尤其是在需要根据扩展名进行操作的场景中。
"""