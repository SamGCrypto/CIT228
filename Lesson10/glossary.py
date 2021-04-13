import json

def menu():
    select = int(input("1-create file, 2-read file, 3-add item to file, 4-quit:  "))
    while select !=1 and select !=2 and select !=3 and select !=4:
        print("Please select a proper option!")
        select = int(input("1-create file, 2-read file, 3-add item to file, 4-quit:  "))
    return select
        
def create_file(object):
    overwriting = input("You are about to create a new file, this will overwrite any previous information(press q to quit, any other key to continue)")
    if overwriting !="q":
        with open("glossary.json","w") as overRideFile:
            json.dump(object, overRideFile, indent=4, sort_keys=True)
            print("glossary.json has been created")

def append_file(add_data):
    try:
        with open("glossary.json","r+") as add_item:
            dictionary = json.load(add_item)
            dictionary.update(add_data)
            add_item.seek(0)
            json.dump(dictionary, add_item,indent=4,sort_keys=True)
            print("information has been added to json file.")
    except FileNotFoundError:
        print("Sorry but there is no file! Try again.")

def read_file():
    try:
        with open("glossary.json") as file:
            dictionary = json.load(file)
    except FileNotFoundError:
        print("No such file available!")
    else:
        for x,y in dictionary.items():
            print(x.title(), " is a ", y)
    
def get_term():
    userResponse = input("Enter a definition of a function in coding: ")
    response = userResponse.lower()
    response.split()[0].title()
    return response

def get_key():
    userResponse = input("Enter in a functions name: ")
    functName = userResponse.title()
    return functName
    
glossary = {
    "dictionary": "python data type that stores key values:value pairs",
    "tuples":"a list of items that do not change.",
    "list": "a list of items that can change.",
    "for":"used to create a counting loop",
    "while":"used to create a conditional loop",
    "int": "variable that should only be a number",
    "bool":"a true or false variable"
}

counter = 0
choice = menu()
while choice != 4:
    if choice == 1:
        create_file(glossary)
    elif choice ==2:
        read_file()
    elif choice ==3:
        key = get_key()
        term = get_term()
        newItemDictionary={key:term}
        append_file(newItemDictionary)
    else:
        print("ERROR option not there.")
    choice = menu()

