"""класс методы, статик методы и инстанс методы"""

# class A:
#     a = None 
#     def __init__(self, b) -> None:
#         self.b = b

# A(12).b
# A.a


# class SomeClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def func(self):
#         pass

#     @classmethod
#     def func_two(cls):
#         pass

#     @staticmethod
#     def func_three():
#         pass

# SomeClass().func()

# DELIVERY_PRICE = 120

# class Order:
#     orders = []

#     def __init__(self, name, address, product, price, count) -> None:
#         self.name = name
#         self.address = address
#         self.product = product
#         self.price = price
#         self.count = count

#     def create_order(self):
#         order = {
#             "name": self.name,
#             "address": self.address,
#             "product": self.product,
#             "price": self.price,
#             "count": self.count,
#             "delivery": self.set_delivery(self.count, DELIVERY_PRICE)
#         }
#         self.orders.append(order)

#     @staticmethod
#     def set_delivery(count, price):
#         return price * count / 2

# order1 = Order(
#     "John", "California", "IceCream", 250, 5
# )
# order2 = Order(
#     "Raychel", "LA", "IceCream", 250, 10
# )
# order1.create_order()
# # print(order1.orders)

# order2.create_order()
# # print(order2.orders)
# print(Order.orders)



# class Pizza:
#     def __init__(self, name, radius, *ingredients):
#         self.name = name
#         self.ingredients = ingredients
#         self.radius = radius
#         self.create_pizza()

#     def create_pizza(self):
#         print(f'Created Pizza -> {self.name} with radius {self.radius} ingredients {self.ingredients}')

#     @classmethod
#     def create_pepperoni(cls, radius):
#         name = "Pepperoni"
#         ingredients = ('sausage', 'cheese', 'dough', 'oregano')
#         return cls(name, radius, *ingredients)                              # создание объкта через класс

#     @classmethod
#     def create_margarita(cls, radius):
#         name = "Margarita"
#         ingredients = ('tomato', 'cheese', 'dough', 'oregano')
#         return cls(name, radius, *ingredients)

#     @classmethod
#     def create_four_cheese(cls, radius):
#         name = "Four Cheese"
#         ingredients = ("cheese anotger", 'cheese', 'dough', "oregano")
#         return cls(name, radius, *ingredients)

# Pizza.create_pepperoni(30)
# Pizza.create_margarita(25)
# Pizza.create_four_cheese(30)



class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

    
v = Vector(1, 2)
res = Vector.get_coord(v)
print(res)









