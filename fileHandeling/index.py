# File open

file = open("data.txt", 'r')
content = file.read()
print(content)

# Read file byte by byte
file.read(10)

# read single line
file.readline()

# close file
file.close()


# Write file
writeFile = open("data.txt", 'w')
writeFile.write('New content written by python')
writeFile.close()


# write and append
open('data.txt', 'a')


# another way to read file

with open('data.txt', 'r') as file:
    contents = file.read()
    print(contents)


# readline() read single line in order of execution
# readlines() read multiple lines and returns list
