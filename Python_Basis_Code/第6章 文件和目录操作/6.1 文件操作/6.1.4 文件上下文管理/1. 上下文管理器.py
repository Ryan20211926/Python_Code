# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/28 22:13
# @Author  : Ryan 
# @File    : 1. 上下文管理器.py
# @Software: PyCharm
"""
"""
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/27 22:05
# @Author  : Ryan
# @File    : 1. 上下文管理.py
# @Software: PyCharm

# 1. **基本语法** 使用 `with` 语句和 `open()` 函数来打开文件，文件对象会在代码块执行完成后自动关闭。

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# 文件在退出 with 代码块后自动关闭

# 4. 例读取文件
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 写入文件
with open("example.txt", "w") as file:
    file.write("Hello, World!")

#### **追加内容**
with open("example.txt", "a") as file:
    file.write("\nThis is a new line.")

#### **读取二进制文件**
with open("example.bin", "rb") as file:
    data = file.read()
    print(data)

#### **写入二进制文件**
with open("example.bin", "wb") as file:
    file.write(b"Hello, binary world!")


"""
在 Python 中，文件上下文管理是一种通过 `with` 语句来安全地打开和操作文件的方式。它能够确保文件在使用完成后正确关闭，即使在文件操作过程中发生异常也是如此。使用上下文管理器可以避免忘记关闭文件而导致的资源泄漏问题，让代码更加简洁、安全和易于维护。

以下是关于 Python 文件上下文管理的详细介绍：

### 2. **优点**
- **自动关闭文件**：即使在文件操作过程中发生异常，文件也会被正确关闭。
- **代码更简洁**：不需要显式调用 `file.close()`。
- **安全性更高**：减少了因忘记关闭文件而导致的资源泄漏风险。

### 3. **支持的文件操作模式**
`open()` 函数支持多种文件操作模式：
- **`r`**：只读模式（默认模式）。
- **`w`**：写入模式，如果文件存在则覆盖内容，不存在则创建新文件。
- **`x`**：独占写入模式，如果文件存在则抛出异常，不存在则创建新文件。
- **`a`**：追加模式，如果文件存在则在文件末尾追加内容，不存在则创建新文件。
- **`t`**：文本模式（默认模式）。
- **`b`**：二进制模式。
- **`+`**：更新模式，用于读写文件。



### 5. **上下文管理器的原理**
在 Python 中，上下文管理器是通过实现 `__enter__` 和 `__exit__` 方法的类来实现的。`with` 语句会自动调用这两个方法：
- **`__enter__`**：在进入代码块时被调用，通常用于初始化资源（如打开文件）。
- **`__exit__`**：在退出代码块时被调用，无论是否发生异常，都会执行，通常用于清理资源（如关闭文件）。

`open()` 函数返回的文件对象本身就是一个上下文管理器，它实现了这两个方法。

### 6. **自定义上下文管理器**
如果需要自定义上下文管理器，可以通过实现 `__enter__` 和 `__exit__` 方法来创建自己的类，或者使用 `contextlib` 模块中的 `contextmanager` 装饰器。

#### **使用类实现**
```python
class MyFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with MyFileManager("example.txt", "r") as file:
    content = file.read()
    print(content)
```

#### **使用 `contextlib`**
```python
from contextlib import contextmanager

@contextmanager
def my_file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with my_file_manager("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### 7. **注意事项**
- **文件路径**：确保文件路径正确，如果文件路径不正确，可能会抛出 `FileNotFoundError`。
- **异常处理**：虽然上下文管理器会自动关闭文件，但在文件操作过程中仍然需要处理可能的异常（如读取文件时文件损坏）。
- **文件模式**：选择合适的文件模式，避免数据丢失或文件损坏。

总之，文件上下文管理是 Python 中处理文件的推荐方式，它让文件操作更加安全、简洁和高效。
"""