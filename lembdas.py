# Lambdas are like function but they dont have any names. It is anonomous func

# Regular func
def square(x):
    return x ** 2


square(2)


# Lambda
result = (lambda x: x ** 2)(8)
print(result)

sum = (lambda x, y: x+y)(2, 3)
print(sum)


# Lambda funtions are those functions that execute at run time
