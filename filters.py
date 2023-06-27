numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = []
for number in numbers:
    if number % 2 == 1:
        odd_nums.append(number)


print(odd_nums)


def odd(x):
    if x % 2 == 1:
        return x


odds = list(filter(odd, numbers))

print(odds)


with_lambda = list(filter(lambda x: x % 2 == 1, numbers))

print(with_lambda)
