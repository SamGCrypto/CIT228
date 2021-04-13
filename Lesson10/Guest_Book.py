while True:
    userName = str(input("Please put your name in here: "))
    data = open("guestBooks.txt","a")
    userName+= "\n"
    data.write(userName)
    data.close()