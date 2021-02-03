###Glossary project with hands on #2

glossary = {
    "dictionary": "Python data type that stores key values:value pairs",
    "tuples":"A list of items that do not change.",
    "list": "A list of items that can change.",
    "for":"used to create a counting loop",
    "while":"used to create a conditional loop"
}


print("Dictionary")
print("\t",glossary["dictionary"])
print("Tuples")
print("\t",glossary["tuples"])
print("list")
print("\t",glossary["list"])
print("For Loops")
print("\t",glossary["for"])
print("While loops")
print("\t",glossary["while"])

#TRY IT YOURSELF NUMBER 6-4
for x,y in glossary.items():
    print(x, ":" ,y)

glossary = {
    "dictionary": "Python data type that stores key values:value pairs",
    "tuples":"A list of items that do not change.",
    "list": "A list of items that can change.",
    "for":"used to create a counting loop",
    "while":"used to create a conditional loop",
    "int": "variable that should only be a number",
    "bool":"A true or false variable"
}

for x,y in glossary.items():
    print(x, ":" ,y)

