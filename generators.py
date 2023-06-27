# Generators are just line normal function but it return itrative

def function():
    counter = 0
    while counter <= 10:
        yield counter
        counter = counter+1


print(list(function()))


def even_generator(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


even = (list(even_generator(10)))

print(even)
