while True:
    num1 = input("Please enter first number: ")
    num2 = input("Please enter second number: ")
    try:
        answer = int(num1)+int(num2)
    except ValueError:
        print("Oops cannot enter a string")
    else:
        print(answer)
        break    