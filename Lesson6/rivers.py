rivers = {'Nile':['Egypt'],'Amazon':['Peru','Ecuador','Columbia','Venezuela','Bolivia','Brazil'],'Yangtze':['China'],'Mississippi River':['America']}
print("-------------Rivers and Countries-----------------")
for x in rivers.items():
    print(f"\n{x}")

print("-------Rivers-----------------")
for x,y in rivers.items():
    print(f"\n{x}")

print("-------Countries-----------------")
for x,y in rivers.items():
    print(f"\n{y}")