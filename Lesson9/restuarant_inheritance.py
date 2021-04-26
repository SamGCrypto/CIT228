class Restaurant:

    def __init__(self, cuisine_type, isOpen, name, numServed=0):
        self.cuisine_type = cuisine_type
        self.isOpen = isOpen
        self.name = name
        self.numServed = numServed

    def describe_restaurant(self):
        print(f"the restaurant {self.name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is {self.isOpen}")

    def number_served(self):
        print(f"Number of people served {self.numServed} at {self.name}")

    def number_served_updated(self, numServed):
        self.numServed += numServed
        
    def set_number_served(self, served):
        self.numServed = int(served)

class IceCreamStand(Restaurant):
    def __init__(self, isOpen, name):
        self.cuisine = 'Ice Cream'
        self.isOpen = isOpen
        self.name = name
        self.flavors = []

    def add_flavors(self):
        while True:
            newFav = str(input("Enter a flavor: "))
            if newFav == 'end':
                break
            else:
                self.flavors.append(newFav)
    
    def list_flavors(self):
        for u in self.flavors:
            print(u)

new_shop = IceCreamStand('Open','The Goofy Goober')
new_shop.describe_restaurant()
new_shop.open_restaurant()
new_shop.add_flavors()
new_shop.list_flavors()