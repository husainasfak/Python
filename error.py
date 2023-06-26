# Types of Errors

# Errors and Exceptions

# Syntax Error

# Logical Error

# Runtime Error
# n = 10
# d = 0
# result = n/d  # ZeroDivisionError: division by zero
# print(result)

# Exception handling
n = 10
d = 0
try:
    result = n/d
except ZeroDivisionError:
    print('There is an error occure')
else:
    print(result)  # runs when exception not run
finally:
    print('These will run no matter what ')
