class Restaurant:

    def __init__(self, cuisine, isOpen, name, numServed=0):
        self.cuisine = cuisine
        self.isOpen = isOpen
        self.name = name
        self.numServed = numServed

    def describe_restaurant(self):
        print(f"the restaurant {self.name} serves {self.cuisine}")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is {self.isOpen}")

    def number_served(self):
        print(f"Number of people served {self.numServed} at {self.name}")

    def number_served_updated(self, numServed):
        self.numServed += numServed
        
    def number_served_default(self, served):
        self.numServed = int(served)

