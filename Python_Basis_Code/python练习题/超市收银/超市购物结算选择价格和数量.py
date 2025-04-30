# coding:utf-8
# @Time    : 2024/12/20 6:52
# @Author  : Ryan
# @FileName: 超市购物结算选择价格和数量.py

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, price, quantity):
        self.items.append({'price': price, 'quantity': quantity})

    def total_cost(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def checkout(self):
        total = self.total_cost()
        print(f"您的总花费是：{total}元。")

def main():
    cart = ShoppingCart()
    while True:
        print("请输入商品的价格和数量（输入'done'结束购物）：")
        price_input = input("价格（元）：")
        if price_input.lower() == 'done':
            break
        quantity_input = input("数量：")
        if quantity_input.isdigit() and price_input.replace('.', '', 1).isdigit():
            price = float(price_input)
            quantity = int(quantity_input)
            cart.add_item(price, quantity)
        else:
            print("输入错误，请确保价格和数量是数字。")

    cart.checkout()

if __name__ == "__main__":
    main()