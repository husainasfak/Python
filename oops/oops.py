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


Inheritance is a powerful tool, but it is a really bad idea to try to overuse it. Inheritance should only be used when every instance of the child class can also be considered the same type as the parent class.

When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance probably is not the best answer. In that case, you would probably just want to share some functions, or maybe make a new parent class that both classes inherit from

we should always be careful that each time we inherit from a base class the child is a strict subset of the parent. You should never think to yourself "my child's class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.

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


# Method Overriding
class Food:
    def type(self):
        print('Food')


class Fruit(Food):
    def type(self):
        print('Fruit')


apple = Fruit()
samosa = Food()

print(apple.type())
print(samosa.type())


# #  operator overloading
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c


# calculator = Calculator()
# calculator.add(2, 3)
# calculator.add(2, 3, 4)


# Instance Method - define inside in constructor


class Student:
    def __init__(self, name):
        self.name = name  # instance varibale

    # this method using instance variable therefor this method is called as instance method. we always pass self in the method, self means instance
    def hello(self):
        print(f'Hello, {self.name}')

    def name_length(self):
        return len(self.name)


Student1 = Student('Ram')
# Instance method always needs to be invoked in an object
Student1.hello()

print(Student1.name_length())


# Class Methods - It uses class variable instead of instance veriable

class Archer:
    # class variable - it is the property of the class
    category = "shooter"

    def __init__(self, name):
        #  Instance varible
        self.name = name

    # Instance method
    def greet(self):
        print(f'Hello, {self.name}')

    # class methods - pass class(cls). we can not inovked it in object
    @classmethod
    def info(cls):
        print(f'{cls.category}')


maria = Archer('maria')

# Invoked class method
Archer.info()


# Static method - it belongs to the class but they do not have access to the instacne and class variables

class Golem:
    category = "attacker"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

    @classmethod
    def info(cls):
        print(f'{cls.category}')

    # Static methods
    @staticmethod
    def attack(speed):
        print(f'I am attacking at {speed} speed')


# Invoked static method - instance or class
got = Golem('Got')
got.attack(200)


# Example of static methods

class Circle:

    @staticmethod
    def area(r):
        return 3.14 * r * r

    @staticmethod
    def circumference(r):
        return 2 * 3.14 * r


a = Circle.area(10)
c = Circle.circumference(10)


# Nested class

class Car:

    def __init__(self, brand):
        self.brand = brand
        # Need to create a object of inner class to access it
        self.Steering_Object = self.Steering()

    @staticmethod
    def drive():
        print('Driving')

    class Steering:
        @staticmethod
        def rotate():
            print('Rotating')


car = Car('ABC')
car.drive()

# acess nested steering class

steering = car.Steering_Object
steering.rotate()


# Constructor inheritence

class Parent:
    def __init__(self):
        self.parent_balance = 5000

    def display_balance(self):
        print(f'Parents balance : {self.parent_balance}')


class Child(Parent):
    pass


#  child class does not have __init__ method but it will inherit that from Parent class
mike = Child()

mike.display_balance()

#  how to access parents method into child class


class Child2(Parent):
    def __init__(self):
        # super function is use to call the parent class into chaild class
        super().__init__()

        self.child_balance = 200

    def display_balance(self):
        print(f'Child balance : {self.child_balance}')

    def total_balance(self):
        print(f"total : {self.parent_balance + self.child_balance}")


#  Encapsulation

        """
        Encapsulation is the practice of hiding information inside a "black box" so that other developers working with the code don't have to worry about it.
        
        In the context of object-oriented programming, we can practice good encapsulation by using private and public members. The idea is that if we want the users of our class to interact with something directly, we make it public. If they don't need to use a certain method or property, we make that private to keep the usage instructions for our class simple.
        """


#  To enforce encapsulation in Python, developers prefix properties and methods that they intend to be private with a double underscore.

class Wall():
    def __init__(self, height):
        # this stops us from accessing the __height
        # property directly on an instance of a Wall
        self.__height = height

    def get_height(self):
        return self.__height


# Abstraction
"""
        Abstraction is one of the key concepts of object-oriented programming. The goal of abstraction is to handle complexity by hiding unnecessary details. As you can see, abstraction and encapsulation typically go hand in hand, and if we aren't careful with our definitions, they can seem like the same thing.
"""

#  ABSTRACTION VS ENCAPSULATION

"""
      - Abstraction is a technique that helps us identify what information and behavior should be encapsulated, and what should be exposed.
      - Encapsulation is the technique for organizing the code to encapsulate what should be hidden, and make visible what is intended to be visible.  
    
    SO ARE WE ENCAPSULATING OR ABSTRACTING OUR CODE WHEN WE MAKE PRIVATE DATA AND METHODS?
    Both. Almost always we are doing both. The process of using the double underscore is an encapsulation method. The process of deciding which data deserves to be hidden behind the double underscore is an abstraction. Let's look at a concrete example.
"""


"""
    HOW OOP DEVELOPERS THINK
    
    As we saw in the last exercise class variables can be private, but methods can be private as well. In other words, we can encapsulate behavior as well as data.

    GROUPING DATA AND BEHAVIOR
    
    Classes in object-oriented programming are all about grouping data and behavior together in one place: an object. Object-oriented programmers tend to think about programming as a modeling problem. They think, "how can I write a Human class that simulates the data and behavior of a real human?"

    We aren't focusing on functional programming in this course, but to provide some contrast, functional programmers tend to think of their code as inputs and outputs. "When a human acts, what are the inputs to that action, and how do the outputs affect my program state?"

    BOTH PARADIGMS ARE VALUABLE
    
    While OOP isn't the only paradigm in programming, it's a tried and true one that is useful in a variety of circumstances. In any event, if you have an understanding of multiple ways of thinking about code, you'll be a much better developer overall.  
        
"""
