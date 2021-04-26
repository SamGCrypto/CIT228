print("-----------HANDS ON 7-8---------------------")
deli_sandwichs = ['Grilled Cheese','Ham','Roast Beef','Pastrami','Italian','Vegan','BLT','Steak','Pastrami','Greek']
finished_sandwichs =[]

for sandwich in deli_sandwichs:
    print(f"I made your {sandwich} sandwich")
    finished_sandwichs.append(sandwich)

print("Sandwiches that were made today include:")
for sandwich in finished_sandwichs:
    print(sandwich)

while 'Pastrami' in deli_sandwichs:
    deli_sandwichs.remove('Pastrami')

print("Sorry we have ran out of Pastrami!")
for sandwich in deli_sandwichs:
    print(f"I made your {sandwich} sandwich")
print("Sandwiches that were made today include:")
for sandwich in finished_sandwichs:
    print(sandwich)