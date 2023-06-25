# Collection of unique elements
# set doent accept int or string it accept iterable like list. set is represent as curly braces. set is unorderd
numbers = set([1, 2, 1, 1, 3, 4, 5, 6, 7, 7])
print(numbers)

# another way to crating a set
nums = {1, 2, 3, 4, 5, 5, 5, 2}


# empty set
s = set()

# if you create empty set using curly brackets. it is not set. it will be dict


# set operations

s = {'a', 'b', 'c', 'd', 'e'}

print('c' in s)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union
set3 = set1.union(set2)
print(set3)

print(set1 | set2)


# Intersection

set4 = set1.intersection(set2)
print(set4)

print(set1 & set2)


# complement or minus

print(set1 - set2)

print(set2 - set1)


# Symmetric differnece -- remove common elements

print(set1 ^ set2)


# Add and remove element in set

s.add('d')
s.remove('a')  # raise error if element is not present
s.discard('a')  # not raise an error

s.pop()  # pop random number in the given set

s.clear()  # remove all entries in the set
