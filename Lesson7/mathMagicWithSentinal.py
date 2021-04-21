import random
incorrect =0
numberCorrect =0
continueTesting = 'yes'
while continueTesting =='yes':
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    randOption = random.randrange(1,2)
    if incorrect >4:
        print("Maybe you should go get a tutor.")
        break
    if randOption ==1:
        correctAnswer = int(randNumber1+randNumber2)
        yourAnswer = int(input(f"What is the interger value of {randNumber1} + {randNumber2}: "))
        if correctAnswer==yourAnswer:
            print("Great job, you answered correctly!")
            numberCorrect+=1
        else:
            print(f"Sorry, the correct answer is {correctAnswer}")
            incorrect+=1
    
    if randOption==2:
        correctAnswer = int(randNumber1-randNumber2)
        yourAnswer = int(input(f"What is the interger value of {randNumber1}-{randNumber2}: "))
        if correctAnswer==yourAnswer:
            print("Great job, you answered correctly!")
            numberCorrect+=1
        else:
            print(f"Sorry, the correct answer is {correctAnswer}")
            incorrect+=1
    print("Do you wish to continue?")
    continueTesting=input()

if incorrect>5:
    print("Try again next time")
else:
    print("You answered", numberCorrect, " Questions correctly!")

print("Thanks for playing.")