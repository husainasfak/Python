# same as object in JS

# Dictionaries are mutable
itemsCount = {"Ball": 4, "Bat": 23}
itemsCount['Bat'] = 10
print(itemsCount["Bat"])


# Built in function to create Dictionary
# Pass key value pair as argument
people = dict(
    john=32,
    rob=45,
    tim=20
)
people["mike"] = 30

del people['rob']

# Dict methods
# Get method not throw an error and dont crash the program when key is not present in the dictionary. It return None when it doesnt find any key
people.get('john')

# Update -  update and add new key value pairs
new_people = {"john": 123, "rin": 12}

people.update(new_people)

# A = people.pop("rob")
# print(A)

print(people.values())  # return list of values
print(people.keys())  # return list of keys
