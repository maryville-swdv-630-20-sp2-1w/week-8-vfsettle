#this module implements a cart iteration for customers to review items before proceeding to payment authorization.
import abc

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "{}: $ {}".format(self.name, self.price)

class CartIterator:
    def __init__(self, items):
        self.index = 0
        self.items = items

    def has_next(self):
        return False if self.index >= len(self.items) else True

    def next(self):
        item = self.items[self.index]
        self.index += 1
        return item

    def remove(self):
        return self.items.pop()

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def iterator(self):
        return CartIterator(self.items)

sku1 = Item("small 2-topping pizza", 7.99)
sku2 = Item("medium 2-topping pizza", 9.99)
sku3 = Item("large 2-topping pizza", 11.99)
sku4 = Item("extra-large 2-topping pizza", 13.99)
sku5 = Item("small specialty pizza", 9.99)
sku6 = Item("medium specialty pizza", 11.99)
sku7 = Item("large specialty pizza", 13.99)
sku8 = Item("extra-large specialty pizza", 15.99)

cart = Cart()
cart.add(sku2)
cart.add(sku8)


print("Cart Inventory:")
iterator = cart.iterator()

while iterator.has_next():
    item = iterator.next()
    print(item)
