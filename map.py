numbers = [1, 2, 3, 4, 5, 6]


def square(x):
    return x*x


# map return object
new_list = list(map(square, numbers))

print(new_list)


str = ["1", "2", "3", "4", "5"]


def convertToInteger(x):
    return int(x)


output = list(map(convertToInteger, str))

print(output)


prices = [100, 200, 300, 400, 500, 600]

priceOutput = list(map(lambda x: x-x*5/100, prices))

print(priceOutput)
