class User:
    def __init__(self, fname, lname, greeting,password,loginAttempt = 0):
        self.fname = fname
        self.lname = lname
        self.greeting = greeting
        self.password = password
        self.loginAttempt = loginAttempt


    def describe_self(self):
        full_name = f"{self.fname} {self.lname}"
        print(f"My name is {full_name}")

    def greet_user(self):
        print(f"{self.fname} {self.lname} says '{self.greeting}'")

    def increment_login_attempts(self):
        self.loginAttempt += 1
    
    def reset_login_attempts(self):
        self.loginAttempt=0

class Admin(User):
    def __init__(self, fname, lname, greeting, password, privileges):
        super().__init__(fname, lname, greeting, password)   
        self.privileges = privileges

    def show_privileges(self):
        for p in self.privileges:
            print(p)


new_admin = Admin('Michael','Kenton','Hello there','passw0rd',['Can modify','Can Delete'])

new_admin.greet_user()
new_admin.describe_self()
new_admin.
new_admin.show_privileges()