import datetime
import random
import greet

from greet import hello, bye

# Custom modules
greet.hello()
hello()

greet.bye()
bye()


# Random module
result = random.randint(1, 10)
print(result)

#  Date time module
print(datetime.date.today())

print(datetime.datetime.now())
