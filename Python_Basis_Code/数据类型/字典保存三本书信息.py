# coding:utf-8
# @Time    : 2024/12/22 8:57
# @Author  : Ryan
# @FileName: 字典保存三本书信息.py

# 初始化一个空字典来保存书籍信息，键为书名，值为另一个包含作者和价格的字典
books = {}

# 定义一个函数来添加书籍
def add_book(books, title, author, price):
    # 检查书名是否已经存在
    if title in books:
        print(f"不能添加书籍：'{title}'，因为已经存在同名书籍。")
    else:
        # 将书籍信息添加到字典中
        books[title] = {'author': author, 'price': price}
        print(f"书籍 '{title}' 已添加。")

# 添加三本书
add_book(books, 'aaa', 'Author A', 100)
add_book(books, 'bbb', 'Author B', 200)
add_book(books, 'aaa', 'Author C', 150)  # 尝试添加同名书籍

# 打印所有书籍信息
print("\n所有书籍信息：")
for title, info in books.items():
    print(f"书名：{title}, 作者：{info['author']}, 价格：{info['price']}")