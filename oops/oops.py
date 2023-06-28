# Create object and class

# Class is blueprint to create objects


# Create class
class Product:

    sameForAll = 200  # class attribute

    # instance Attribute --> Different for every object instance. it will automatically invoked whenever object created

    def __init__(self, name, price):
        # self - refrence of object
        self.name = name
        self.price = price

    def summer_discount(self, discount_percent):
        self.price = self.price - self.price * discount_percent/100


# Craete object using class
p1 = Product("Iphone", 300)

print(p1.name)
print(p1.price)
p1.summer_discount(5)
print(p1.price)

p2 = Product('Ipad', 300)
print(p1.name)
print(p1.price)
p1.summer_discount(10)
print(p1.price)


# Inheritance
