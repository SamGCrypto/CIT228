with open("learningPython.txt") as file_object:
    contents = file_object.read()
print(contents)

with open("learningPython.txt") as file_object:
    for line in file_object:
        print(line)
with open("learningPython.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

with open("learningPython.txt") as file_object:
    for line in file_object:
        print(line.replace("Python","Java"))