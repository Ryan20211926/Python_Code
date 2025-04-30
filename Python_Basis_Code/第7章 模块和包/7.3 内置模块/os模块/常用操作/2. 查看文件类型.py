# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 22:21
# @Author  : Ryan 
# @File    : 2. 查看文件类型.py
# @Software: PyCharm
"""
在 Python 中，查看文件类型可以通过多种方法实现，常见的方法包括：
1. **通过扩展名判断文件类型**：使用 `os.path.splitext()` 获取文件扩展名，然后根据扩展名判断文件类型。
2. **使用 `mimetypes` 模块**：通过扩展名获取文件的 MIME 类型。
3. **使用 `magic` 模块**：通过文件内容（而不是扩展名）来判断文件类型。

以下是每种方法的示例代码：

### 方法 1：通过扩展名判断文件类型
这种方法简单高效，但依赖于文件扩展名的准确性。

```python
import os

def get_file_type_by_extension(filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()  # 转换为小写以避免大小写问题
    if ext in ['.txt', '.doc', '.docx']:
        return "Text Document"
    elif ext in ['.jpg', '.jpeg', '.png', '.gif']:
        return "Image"
    elif ext in ['.mp3', '.wav']:
        return "Audio"
    elif ext in ['.mp4', '.avi', '.mov']:
        return "Video"
    elif ext in ['.pdf']:
        return "PDF Document"
    else:
        return "Unknown"

# 示例
filename = "example.txt"
file_type = get_file_type_by_extension(filename)
print(f"The file '{filename}' is a {file_type}.")
```

### 方法 2：使用 `mimetypes` 模块
`mimetypes` 模块可以根据文件扩展名返回文件的 MIME 类型，这是一种更通用的方法。

```python
import mimetypes

def get_file_type_by_mime(filename):
    mime_type, _ = mimetypes.guess_type(filename)
    if mime_type:
        return mime_type
    else:
        return "Unknown"

# 示例
filename = "example.txt"
file_type = get_file_type_by_mime(filename)
print(f"The MIME type of '{filename}' is {file_type}.")
```

### 方法 3：使用 `magic` 模块
`magic` 模块可以通过文件的内容（而不是扩展名）来判断文件类型。这种方法更准确，但需要安装 `python-magic` 库。

#### 安装 `python-magic`
```bash
pip install python-magic
```

#### 示例代码
```python
import magic

def get_file_type_by_magic(filename):
    # 创建一个 magic.Magic 对象
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(filename)
    return file_type

# 示例
filename = "example.txt"
file_type = get_file_type_by_magic(filename)
print(f"The file type of '{filename}' is {file_type}.")
```

### 方法 4：结合多种方法
在实际应用中，可以结合扩展名和 MIME 类型来提高判断的准确性。

```python
import os
import mimetypes

def get_file_type(filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    mime_type, _ = mimetypes.guess_type(filename)

    if ext in ['.txt', '.doc', '.docx']:
        return "Text Document"
    elif ext in ['.jpg', '.jpeg', '.png', '.gif']:
        return "Image"
    elif ext in ['.mp3', '.wav']:
        return "Audio"
    elif ext in ['.mp4', '.avi', '.mov']:
        return "Video"
    elif ext in ['.pdf']:
        return "PDF Document"
    elif mime_type:
        return mime_type
    else:
        return "Unknown"

# 示例
filename = "example.txt"
file_type = get_file_type(filename)
print(f"The file '{filename}' is a {file_type}.")
```

### 总结
- 如果只需要简单判断文件类型，可以通过扩展名来实现。
- 如果需要更准确的判断，可以使用 `mimetypes` 模块。
- 如果需要根据文件内容判断类型，可以使用 `magic` 模块。
- 结合多种方法可以提高判断的准确性和灵活性。
"""