import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
tempsJune = [99,86,87,88,111,86,103,87,94,78,77,85,88,82,85,85,88,89,89,90,89,78,80,81,82,83,82,83,84,85]
tempsJuly = [100,105,84,105,90,99,90,95,94,100,79,112,99,100,101,100,99,97,96,98,97,92,89,88,88,86,87,85,86,88]
tempsJan = [10,8,15,11,23,33,23,44,30,32,34,35,34,35,22,32,34,35,34,35,32,34,35,34,35,32,34,35,34,35,]
tempsFeb=[19,21,18,22,23,25,29,30,33,35,55,56,60,55,58,55,56,52,51,50,50,49,48,48,45,44,42,41,40,41]

ax=plt.subplot()
ax.scatter(tempsJan, days, c=days, cmap=plt.cm.viridis,s=150,label="Jan scores")
ax.scatter(tempsFeb, days,c=days, cmap=plt.cm.inferno,s=200,label="Feb scores")
ax.scatter(tempsJune, days, c=days, cmap=plt.cm.plasma,s=100,label="June scores")
ax.scatter(tempsJuly, days,c=days, cmap=plt.cm.RdPu,s=50,label="July scores")
plt.ylabel("Points")
plt.xlabel("Temps")
plt.suptitle("Temperature test over days.")
plt.title("Jan-Feb vs June-July")
plt.legend(loc='lower center',ncol=30,fontsize=8)

plt.grid()
plt.show()