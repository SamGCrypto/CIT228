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
for t in transportation:
    print(t)
for t in accomodations:
    print(t)
for t in destinations:
    print(t)
trips=[destinations,accomodations,transportation]
for t in trips:
    print(t)
