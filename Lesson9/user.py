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


badTypist = User('Elle','McEl',13,"5'6",'Hello there','passw0rd')
counter = 0
attempt =10

while counter<attempt:
    print('ERROR WRONG PASSWORD')
    badTypist.increment_login_attempts()
    print(f'User has attempted to enter password {badTypist.loginAttempt}')
    counter+=1
    if counter>5:
        badTypist.reset_login_attempts()
        print(f"The admins have reset login attempts for {badTypist.fname} {badTypist.lname}")
        print(badTypist.loginAttempt)
        break