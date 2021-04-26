import random
monster = ['griffon','dragon','ghost','zombie','vampire']
print("-------list of monsters----------")
for x in monster:
    print(x)
monster.sort()
print()
print("Sorted Monsters")
for x in monster:
    print(x)
print()
notMake = random.randint(0, len(monster)-1)
print("This is a monster that isn't scary")
print(f"{monster[notMake]}")
monster.remove(monster[notMake])
print("Removing not scary monster")
print("Here is a list of all scary monsters")
for x in monster:
    print(x)
print()
print("We are going to remove the last monster on the list.")
monster.pop(-1)
print(f"Here is the list {sorted(monster)}")
print("Lets add in Ghouls to the end and add in Red Cap at the beginning")
monster.append("Ghouls")
monster.insert(0, "Red Cap")
print(monster)