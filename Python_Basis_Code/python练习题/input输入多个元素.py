# coding:utf-8
# @Time    : 2024/12/22 9:04
# @Author  : Ryan
# @FileName: input输入多个元素.py

# 初始化一个空列表来保存书籍信息
books = []

# 提示用户输入书籍信息，并以空格分隔
print("请输入书籍信息（书名 作者 价格），以空格分隔。输入'done'结束输入。")

while True:
    # 获取用户输入的一行文本
    input_line = input("请输入书的基本信息\n")

    # 检查用户是否想要结束输入
    if input_line.lower() == 'done':
        break

    # 分割输入的字符串，获取书名、作者和价格
    try:
        book_info = input_line.split()
        if len(book_info) < 3:
            raise ValueError("输入的信息不完整，请确保输入了书名、作者和价格。")

        # 分别赋值给书名、作者和价格
        title, author, price_str = book_info[0], book_info[1], book_info[2]

        # 将价格字符串转换为浮点数
        price = float(price_str)

        # 将书籍信息作为一个字典添加到列表中
        books.append({'title': title, 'author': author, 'price': price})

        print(f"书籍 '{title}' 已添加。")
    except ValueError as e:
        print(e)

# 打印所有书籍信息
print("\n所有输入的书籍信息如下：")
for book in books:
    print(f"书名：{book['title']}, 作者：{book['author']}, 价格：{book['price']}")