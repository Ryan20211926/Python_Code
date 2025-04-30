# coding:utf-8
# @Time    : 2024/12/19 13:39
# @Author  : Ryan
# @FileName: 添加商品到购物车并支付.py

# 定义商品信息和支付方式优惠
class Supermarket:
    def __init__(self):
        self.cart = []
        self.payment_methods = {
            "1": {"name": "现金支付", "discount": 0.00},
            "2": {"name": "信用卡支付", "discount": 0.05},
            "3": {"name": "微信支付", "discount": 0.03},
            "4": {"name": "支付宝支付", "discount": 0.04}
        }

    def add_item_to_cart(self):
        # 添加商品到购物车
        price_per_item = float(input("请输入商品的单价（元）："))
        quantity = int(input("请输入商品的数量："))
        self.cart.append({"price": price_per_item, "quantity": quantity})

    def calculate_total(self):
        # 计算总价格
        total = sum(item["price"] * item["quantity"] for item in self.cart)
        return total

    def checkout(self):
        # 结账过程
        total_price = self.calculate_total()
        print(f"商品总价为：{total_price}元")

        # 用户选择支付方式
        payment_method = input("请选择支付方式（1：现金支付，2：信用卡支付，3：微信支付，4：支付宝支付）：")

        # 检查支付方式是否有效
        if payment_method in self.payment_methods:
            discount = self.payment_methods[payment_method]["discount"]
            print(f"您选择了{self.payment_methods[payment_method]['name']}，享受{discount * 100}%的优惠。")

            # 计算优惠后的支付金额
            discounted_price = total_price * (1 - discount)
            print(f"优惠后的支付金额为：{discounted_price:.2f}元")

            # 用户输入支付金额
            paid_amount = float(input("请输入您的支付金额（元）："))

            # 计算找零
            if paid_amount >= discounted_price:
                change = paid_amount - discounted_price
                print(f"收您{paid_amount}元，找您{change:.2f}元。")
            else:
                print("支付金额不足，请支付更多。")
        else:
            print("无效的支付方式，请重新选择。")


# 创建超市实例
supermarket = Supermarket()

# 添加商品到购物车
num_items = int(input("您要购买的商品数量："))
for _ in range(num_items):
    supermarket.add_item_to_cart()

# 结账
supermarket.checkout()