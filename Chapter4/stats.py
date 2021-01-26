import random
number = []
for x in range(50):
    number.append(random.randrange(10,100))
print(number)
print(f"The largest number is {max(number)}")
print(f"The smallest number is {min(number)}")
print(f"The total of all the numbers is {sum(number)}")
print(f"The average of all the numbers is {max(number)/len(number)}")

