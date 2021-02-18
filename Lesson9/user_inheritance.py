class User:
    def __init__(self, fname, lname, age, height, greeting,password,loginAttempt = 0):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height
        self.greeting = greeting
        self.password = password
        self.loginAttempt = loginAttempt


    def describe_self(self):
        full_name = f"{self.fname} {self.lname}"
        print(f"{full_name} is roughly {self.age} years old and {self.height} in height.")

    def greet_user(self):
        print(f"{self.fname} {self.lname} says '{self.greeting}'")

    def increment_login_attempts(self):
        self.loginAttempt += 1
    
    def reset_login_attempts(self):
        self.loginAttempt=0

class Admin(User):
    def __init__(self, fname, lname, age,height,password,privilegesList,loginAttempt=0):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height
        self.password = password
        self.loginAttempt = loginAttempt
        self.privilegesList = privilegesList


    def list_privileges(self):
            print(self.privilegesList)        





new_admin = Admin('Michael','Kenton',25,"5'6", 'passw0rd','Can modify')

new_admin.list_privileges()