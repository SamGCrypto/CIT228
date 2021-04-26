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
    def __init__(self, fname, lname, age, height, greeting,password):
        super().__init__(fname, lname, age, height, greeting,password,loginAttempt = 0)
        self.privileges =[]

    def show_privileges(self):
        print("\nPrivileges:")
        for privileges in self.privileges:
            print("- "+privileges)

test = Admin('Alan', 'Michl',10,120,"Hello I am the admin","password")
test.describe_self()

test.privileges = [
    'can rest passwords',
    'can moderate',
    'can suspend accounts',
]
test.show_privileges()