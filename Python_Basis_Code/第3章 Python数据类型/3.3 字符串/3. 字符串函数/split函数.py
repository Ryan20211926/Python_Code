# coding:utf-8
# @Time    : 2025/4/27 12:58
# @Author  : Ryan
# @FileName: split函数.py


# split()可以基于指定分隔符将字符串分隔成多个子字符串(存储到列表中)。如果不指定分隔符，则默认使用空白字符(换行符/空格/制表符)。

# 示例 1：默认分隔符（空白字符）
text = "Hello, World! Welcome to Python."
words = text.split()
print(words)
# 输出：['Hello,', 'World!', 'Welcome', 'to', 'Python.']

# 示例 2：指定分隔符
text = "apple,banana,cherry"
fruits = text.split(',')
print(fruits)
# 输出：['apple', 'banana', 'cherry']

# 示例 3：指定分隔符和最大分割次数
text = "one-two-three-four"
parts = text.split('-', 2)
print(parts)
# 输出：['one', 'two', 'three-four']

# 示例 4：处理连续的分隔符
text = "one  two    three"
words = text.split()
print(words)
# 输出：['one', 'two', 'three']


# 分隔符不存在时：如果字符串中不包含指定的分隔符，split() 函数将返回包含原始字符串的列表。
text = "HelloWorld"
words = text.split("-")
print(words)
# 输出：['HelloWorld']

# 分隔符为空字符串时：如果分隔符是空字符串，split() 函数会抛出 ValueError 异常
text = "Hello, World!"
words = text.split("")  # 这将抛出 ValueError

# 处理字符串末尾的分隔符：如果字符串以分隔符结尾，split() 函数会在结果列表中包含一个空字符串。
text = "Hello, World!  "
words = text.split()
print(words)
# 输出：['Hello,', 'World!', '']

str = "this is string example....wow!!!"
print (len(str.split( )),str.split( ))       # 以空格为分隔符
print (len(str.split('i',1)),str.split('i',1))   # 以 i 为分隔符
print (str.split('w'))     # 以 w 为分隔符
print(len(str.split(None,1)),str.split(None,1)) #以空格分割,但只分割一次
print(len(str.split(None,0)),str.split(None,0)) ##相当于不分割