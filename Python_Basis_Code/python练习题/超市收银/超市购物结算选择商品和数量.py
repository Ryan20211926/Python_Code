# coding:utf-8
# @Time    : 2024/12/20 6:55
# @Author  : Ryan
# @FileName: 超市购物结算选择商品和数量.py
class Supermarket:
    def __init__(self):
        self.products = {
            'apple': 10,
            'banana': 20,
            'bread': 30,
            'milk': 40,
            'eggs': 50
        }
        self.cart = []

    def show_products(self):
        print("Available products:")
        for product, price in self.products.items():
            print(f"{product}: {price}元")

    def add_to_cart(self):
        product = input("Enter the product name (or 'done' to finish shopping): ").lower()
        if product == 'done':
            return False
        if product in self.products:
            quantity = int(input(f"How many {product}s would you like to buy? "))
            if quantity > 0:
                self.cart.append({'product': product, 'quantity': quantity})
                print(f"Added {quantity} {product}(s) to your cart.")
            else:
                print("Please enter a valid quantity.")
            return True
        else:
            print("Sorry, we don't have that product.")
            return True

    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += item['quantity'] * self.products[item['product']]
        return total

    def checkout(self):
        print("Your shopping cart:")
        for item in self.cart:
            print(f"{item['quantity']} x {item['product']} at {self.products[item['product']]}元 each")
        total = self.calculate_total()
        print(f"Total cost: {total}元")

# Create an instance of the Supermarket
market = Supermarket()

# Show available products
market.show_products()

# Shopping loop
while market.add_to_cart():
    pass  # The add_to_cart method handles the loop control

# Checkout
market.checkout()