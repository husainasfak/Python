# function - block of code which does particular task

# defining function

# def hello(name, age=10):
#     print('hello', name, 'your age is', age)


# hello('Asfak')


# # keyword arguments

# def speed(distance, time):
#     return distance/time


# my_speed = speed(time=2, distance=100)


# # return multiple values

# def circle(r):
#     area = 3.14 * r * r
#     circumference = 2 * 3.14 * r
#     return area, circumference


# ar, ci = circle(10)


# # global and local


# count = 10


# def increment():
#     global count
#     count = count+1
#     print(count)


# increment()


# # Variable length positional argument

# def add(*args):  # now we can pass any number of arguments
#     # whenever we pass variable length argument python stores those argument as tuples
#     sum = 0
#     for n in args:
#         sum = sum + n
#     return sum


# print(add(2, 3, 10))


# # Variable length keyword arguments

# def product(**kwargs):
#     # whenever we pass variable length keyword argument python stores those argument as dict

#     for key, value in kwargs.items():
#         print(key + " : " + value)


# product(name="iphone", price="$8000")
# product(name="samsung", price="$800")


# Decorators

"""
     A decorator is a design pattern in Python that allows a user to add or modify new functionality to an existing function or class without modifying its source code. Decorators are usually called before the definition of a function you want to decorate
"""


def log_func_call(func):
    def wrapper(*args, **kwargs):
        print(f"calling func {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finish calling func {func.__name__}")
    return wrapper


@log_func_call
def greet(name):
    print(f"hello, {name}")


greet('Alice')


def summer_discount_decorator(func):
    def wrapper(price):
        func(price)
        return func(price/2)
    return wrapper


@summer_discount_decorator
def total(price):
    return price


print(total(100))
