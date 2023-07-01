# Create object and class

# Class is blueprint to create objects
# Abstraction
# Inheritance
# Polymorphism
# Encapsulation

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

    def get_data(self):
        self.name = input('Enter name of the product ')
        self.price = input('Enter price of the product ')

    def put_data(self):
        print(self.name)
        print(self.price)


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

"""
Inheritance is a fundamental concept that allows classes to inherit properties and behaviors from other classes. It promotes code reusability, modularity, and extensibility. 
     
"""
# Digital Product class inherit all props and method from product class


class DigitalProduct(Product):
    # write pass keyword if dont have any attributes and method
    def __init(self, link):
        self.link = link

    def get_link(self):
        self.link = input("Enter product link: ")

    def put_link(self):
        print(self.link)


ebook = DigitalProduct("", "")
ebook.get_data()
ebook.put_data()
ebook.get_link()
ebook.put_link()

# Multiple Inheritance


class A:
    def method_a(self):
        print('Method of class A')


class B:
    def method_b(self):
        print('method of class B')


class C(A, B):
    def method_c(self):
        print('Method of class c')


cObject = C()
cObject.method_a()
cObject.method_b()
cObject.method_c()


# Multi level Inheritence
# We know one class can inherit props and method of another class but in Multi-level inheritance is a concept in object-oriented programming where a derived class inherits from another derived class. This creates a hierarchy of classes, with each derived class inheriting properties and behaviors from its parent class

class D:
    def method_d(self):
        print('Method of class D')


class E(D):
    def method_e(self):
        print('Method of class E')


class F(E):
    def method_f(self):
        print('Method of class F')


#  In this example class E can access methods of class D. and class F can access methods of class E and D

fObject = F()
fObject.method_d()


# Polymorphism
#  In simple words, Polymorphism is the ability of a variable, function or object to take on multiple forms. For example, in a programming language that supports inheritance, classes in the same hierarchical tree may have methods with the same name but different behaviors.

# Polymorphism is a key concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables objects to be used interchangeably, providing flexibility and extensibility to the code.

# Exmaple of Operator polymorphism
print(1 + 2)  # + operator add two numbers
print("Hello" + "world")  # + operator concatenate two strings


# Example of method Polymorphism
print(len("Hellowrld"))  # Calculate number of char in string
print(len(['Apple', 'Mango', 'Banana']))  # Calculate number of items in list
