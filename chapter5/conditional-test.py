breakfast = ['pancake','egg','bacon','sausage','hashbrown']
if 'pancake' in breakfast: 
    located = True
else:
    located = False
print("=============True results==============")
print(f"10< 20 is {10<20}")
print(f"10<= 20 is {10<=20}")
print(f"10 != 20 is {10!=20}")
print(f"Orange == Orange {'Orange' == 'Orange'}")
print(f"orange == orange {'orange' == 'orange'}")
print(f"Pancake is in the breakfast list? {located}")
print("=============False results=================")
if 'grits' in breakfast: 
    located = True
else:
    located = False
print(f"10> 20 is {10<20}")
print(f"10>= 20 is {10<=20}")
print(f"10 == 20 is {10!=20}")
print(f"Orange != Orange {'Orange' == 'Orange'}")
print(f"orange == ORANGE {'orange' == 'ORANGE'}")
print(f"Grits is in the breakfast list? {located}")
