# coding:utf-8
# @Time    : 2024/12/22 8:36
# @Author  : Ryan
# @FileName: 列表字典保存书信息.py

# 初始化一个空列表来保存多本书的信息
books = []

# 使用循环让用户可以输入多本书的信息
while True:
    # 提示用户输入书籍信息的键
    book_info = {}
    print("请输入书籍信息（输入'done'结束输入）：")
    book_info['title'] = input("书名：")
    if book_info['title'].lower() == 'done':
        break
    book_info['price'] = input("价格：")
    if book_info['price'].lower() == 'done':
        break
    book_info['author'] = input("作者：")
    if book_info['author'].lower() == 'done':
        break
    book_info['publisher'] = input("出版社：")
    if book_info['publisher'].lower() == 'done':
        break

    # 将当前书籍的信息字典添加到列表中
    books.append(book_info)

# 打印所有书籍的信息
print("\n所有输入的书籍信息如下：")
for book in books:
    print("书名:", book['title'])
    print("价格:", book['price'])
    print("作者:", book['author'])
    print("出版社:", book['publisher'])
    print("-" * 30)  # 打印分隔线