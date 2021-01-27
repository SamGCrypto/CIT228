print("---------Exercise 5-8 where list has user-----------")
users=['shaggy','scooby','daphne','fred','admin']
for user in users:
    if 'admin' == user:
        print("Greeting Admin would you like to see a status report?")
    else:
        print(f"Hello {user.capitalize()} thank you for logging in")
print("-----------Exercise 5-9 where list is empty----------------")
users = []
if users:
    print("this list has users")
else:
    print("ERROR: No users available")

print("-------------Exercise 5-10 checking username----------------")
current_users = ['john','anderson','freddy', 'william','joseph']
new_users = ['Marie','joHn','Mary','WILLIAM','Sarah']
i=0
while(i< len(new_users)):
    holding = new_users[i].lower()
    print(new_users[i].lower())
    new_users[i] = holding
    i+=1
for new_user in new_users:
    print(f"Lets see if {new_user} is available")
    if new_user in current_users:
        print("Sorry that user is taken, please rename yourself.")
    else:
        print("That username is available.")