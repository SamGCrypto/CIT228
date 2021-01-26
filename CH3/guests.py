import random
print("---------------Exercise 3-4--------------")
guest = ['Dad', 'Grandma', 'The Count', 'Ghosts']

for x in guest:
    print(f"{x} is invited to dinner")

print("------------Exercise 3-5---------------")
notMake = random.randint(0, len(guest)-1)
guest = ['Dad', 'Grandma', 'The Count', 'Ghosts']
for x in guest:
    print(f"{x} is invited to dinner")
print()
for x in guest:
    if guest[notMake] != x:
        print(f"{x} can make it to dinner.")
    if guest[notMake] == x:
        print(f"{x} cannot make it to dinner.")
        cannotCome = x
guest.remove(cannotCome)
print()
for x in guest:
    print(f"{x} is invited to dinner")
print()
print("------------------Exercise 3-6-----------------")
print("Welp found a bigger table, maybe I should invite more people.")
guest.insert(0,"Pigman")
guest.insert(2, "Victor Frankenstein")
guest.append("Enderman")
print(f"guess I will invite {len(guest)}")
for x in guest:
    print(f"{x} is invited to dinner")
