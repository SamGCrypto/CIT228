class Restaurant:

    def __init__(self, cuisine, isOpen, name):
        self.cuisine = cuisine
        self.isOpen = isOpen
        self.name = name
        self.numServed =0

    def describe_restaurant(self):
        print(f"the restaurant {self.name} serves {self.cuisine}")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is {self.isOpen}")

    def number_served(self):
        print(f"Number of people served {self.numServed} at {self.name}")

    def number_served_updated(self, numServed):
        self.numServed += numServed


        


my_new_res1 = Restaurant('Asian','Open','Thai Kitchen')
my_new_res2 = Restaurant('Mexican','Closed','Taco Bell')
my_new_res3 = Restaurant('BBQ','Open','Big Als BBQ')

print()
my_new_res1.describe_restaurant()
my_new_res1.open_restaurant()

print()
my_new_res2.describe_restaurant()
my_new_res2.open_restaurant()

print()
my_new_res3.describe_restaurant()
my_new_res3.open_restaurant()

my_new_res3.number_served()
my_new_res3.number_served_updated(31)
my_new_res3.number_served() 
my_new_res3.number_served_updated(31)
my_new_res3.number_served() 