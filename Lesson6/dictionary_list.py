destinations={
    "France":"Paris",
    "America":"New Vegas",
    "UK":"London",
    "Mexico":"Cancun",
    "Canada":"Vancouver"
}
accomodations={
    "Type":"AirBNB",
    "Length":"2 Week",
    "Bedroom":"3+",
    "Restrooms":"1+",
    "Kitchen":"Yes",
    "WiFi":"Yes",
    "Laundry":"Yes"
}
transportation={
    "Rental":"Motorcycle",
    "Size":"2 passenger",
    "Miles":"Unlimited"
}

trips=[destinations,accomodations,transportation]
for t in trips:
    print(t)

rivers = {'Nile':['Egypt'],
'Amazon':['Peru','Ecuador','Columbia','Venezuela','Bolivia','Brazil'],
'Yangtze':['China'],
'Mississippi River':['America']}
for key, value in rivers.items():
    if type(value)==list:
        print(f"The {key.title()} river flows through: ")
        for v in value:
            print("\t\t\t\t",v)
        else:
            print(f"The {key.title()} river flows through {value}")