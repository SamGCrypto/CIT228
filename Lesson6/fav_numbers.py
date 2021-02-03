
fav_number = {'Lisa': 13, 'Michael': 60, 'Elisa':68,'Mary':100}
userName = ['Lisa','Michael','Elisa','Mary']
i=0
print(fav_number)
while(i<len(userName)):
    print(f"{userName[i]} favorite number is {fav_number[userName[i]]}")
    i=i+1
