monsters={
    "Mon1":{
        "name":"Vampire",
        "threat":"Yes",
        "scary":"No",
    },
    "Mon2":{
        "name":"Ghost",
        "threat":"No",
        "scary":"Yes",
    },
    "Mon3":{
        "name":"Wil-o-wisp",
        "threat":"Yes",
        "scary":"No",
    },
    "Mon4":{
        "name":"Pixie",
        "threat":"Yes",
        "scary":"No",
    }
}
for mon, info in monsters.items():
    print(f"Monster: {info['name']}")
    threat= info['threat']
    scary = info['scary']
    print(f"Threat: {threat}")
    print(f"Scary: {scary}")