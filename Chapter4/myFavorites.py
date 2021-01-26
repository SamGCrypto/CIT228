print("-------------CH4--Hands on 1---------------------------")
food = ['lasgana','pizza','popcorn','chili','tacos','spaghetti']
numLuck = ['13','68','12','25','15','18']
movList =['The Hobbit','Saw','Nightmare on Elm Street']
comList =['Lasgana','pizza','saw','The Hobbit','13','68']
animal =['duck', 'platypus', 'lizard','goose']
print("favorite food")
print("-----------------------------------------------")
for x in food:
    print(x)
print()

print("favorite number")
print("-----------------------------------------------")
for x in numLuck:
    print(x)
print()

print("favorite movies")
print("-----------------------------------------------")
for x in movList:
    print(x)
print()

print("Combination List")
print("-----------------------------------------------")
for x in comList:
    print(x)

print()
print("favorite animals")
print("----------------------------------------------")
for x in animal:
    if x == 'platypus':
        print(f"{x} is a......")
        print("this one feels like its spying on me.")
    else:
        print(f"{x} is a nice animal")
print("These animals are all good animals....")
print("except the platypus....it feels like its watching me.")