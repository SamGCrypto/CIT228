farmAnimal = ['duck', 'chicken','cow','wilson','turkey']
newFarmAnimal= farmAnimal[:] 
newFarmAnimal.append('rooster')
newFarmAnimal.append('sheep')
newFarmAnimal.append('dog')
newFarmAnimal.append('cat')
print("-------------farm animals-----------")
for x in farmAnimal:
    print(x)
print("----------new farm animals-----------")
for x in newFarmAnimal:
    print(x)
print(f"the first 3 items in the new list are {newFarmAnimal[:3]}")
print(f"the middle 3 items in the new list are {newFarmAnimal[3:6]}")
print(f"the last 3 items in the new list are {newFarmAnimal[6:9]}")