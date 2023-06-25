#  Similar to Arrays in java or c or javascript
# list is Ordered collections of items 

people = ['Ashfak', 'Hussain']

print(people)


# Storing different Datatypes

items = ['Computer',10,4.5,True,'Race car',123]

print(items[2])
print(items[-1]) # last element

a = [1,2]
b = [1,2]

print(a==b) # true


# Slicing the list  -  Accessing the perticular part of the list

print(items[2:5]) # index 2 to 4
print(items[-3:-1]) #index -3 to -2
print(items[-3:]) # index -3 to end of the list

print(items[-1:-3]) # empty list


# in and not operators -- in is case sensetive 

print('Computer' in items) # TRUE
print('Computer' not in items) # TRUE



# functions

print(len(items)) # 6
items.insert(1,'Python') # @ particular index
items.append('GO') # @ last
items.append(['React','Nextjs']) # @ last and add as a another list
items.extend(['Vue','Venilla JS'])

# Append and extend both used for adding element in the list at last. Append is used for adding single element in the list. It takes a single argument and modifies the original list by adding the element as a single item. The extend() method is used to add multiple elements to the end of a list. It takes an iterable (e.g., another list, tuple, or any other iterable object) as an argument and appends each element from the iterable to the original list.

items.remove('Vue')
items.pop()
# items.index('Venilla JS') # find the index of element

scores = [1,2,3,455,321,3]
print(max(scores))
print(min(scores))




# Adding and multiplication in list

a = [ 1,2,3]
b = [4,5,6]

c = a+b # + works as extend or combine

print(c)
print(a*3) # make a three copy of the elements


# Nesting of list

nesting  = [1,2,[3,4,5],6,7,[8,9],10,[11,[12,13]]]

print(nesting[2][2]) # 5
print(nesting[5][0]) # 8
print(nesting[7][1][0]) #12


# mutability of list - list value can be change

mute = [1,2,3]
mute[1] = 200
mute[0:4] =  [10,20,30]
print(mute)