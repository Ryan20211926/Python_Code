# coding:utf-8
# @Time    : 2024/12/21 20:54
# @Author  : Ryan
# @FileName: 列表保存购物信息.py

# 初始化三个空列表来存储商品信息
product_names = []
product_prices = []
product_quantities = []

# 获取用户输入的商品信息
while True:
    product_name = input("请输入商品名称（输入'q'结束输入）：")
    if product_name.lower() == 'q':  # 如果用户输入'q'，则结束输入
        break
    try:
        product_price = float(input("请输入商品价格："))
        product_quantity = int(input("请输入商品数量："))
        # 将商品信息添加到对应的列表中
        product_names.append(product_name)
        product_prices.append(product_price)
        product_quantities.append(product_quantity)
    except ValueError:  # 如果输入的价格或数量不是数字，则提示错误并继续
        print("输入错误，请输入有效的数字。")

# 打印列表内容
print("商品名称:", product_names)
print("价格:", product_prices)
print("数量:", product_quantities)