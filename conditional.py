age = 15

if age >= 18:
    print('You can vote')
else:
    print('You can\'t vote')


mana = 'red'

if mana == 'blue':
    print('A')
elif mana == 'red':
    print('B')
else:
    print('C')


#  Nested if
a = 10
b = 20

if a > 5:
    if b > 15:
        print('B is greater then A')


# Range function


number = list(range(11))
print(number)  # Print number 0 to 10

# number 1 to 10
range(1, 11)

# skiping numbers
range(1, 11, 2)  # it skip 2 numbers in every steps

# For loop

for x in range(5):
    print(x)

# Loop in list
animes = ['One piece', 'Black clover', 'Demon slayer', 'Naruto']
# print(animes)
for anim in animes:
    print(anim)


# loop in dic
people_with_age = {'A': 32, 'B': 12, 'C': 18}


for people in people_with_age:
    print('keys : ', people)
    print('Values : ', people_with_age[people])


# while loop

counter = 0
while counter <= 10:
    print(counter)
    counter += 1
