import random
problems = int(input("How many math problems would you like to practice?"))
counter = 0
numberCorrect =0
while counter<problems:
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    randOption = random.randrange(0,1)
    if randOption ==0:
        correctAnswer = int(randNumber1+randNumber2)
        yourAnswer = int(input(f"What is the interger value of {randNumber1} + {randNumber2}: "))
        if correctAnswer==yourAnswer:
            print("Great job, you answered correctly!")
            numberCorrect+=1
        else:
            print(f"Sorry, the correct answer is {correctAnswer}")
    if randOption==1:
        correctAnswer = int(randNumber1-randNumber2)
        yourAnswer = int(input(f"What is the interger value of {randNumber1}-{randNumber2}: "))
        if correctAnswer==yourAnswer:
            print("Great job, you answered correctly!")
            numberCorrect+=1
        else:
            print(f"Sorry, the correct answer is {correctAnswer}")

print("You answered", numberCorrect, " Questions correctly!")
print("Thanks for playing.")