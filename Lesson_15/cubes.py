import matplotlib.pyplot as plt

squared=[]
cubed=[]
inputVal =[1,2,3,4,5]
for num in inputVal:
    squared.append(num*num)
for num in inputVal:
    cubed.append(num*num*num)

plt.suptitle("Cubed and Squares")
plt.subplots_adjust(top=.8,wspace=1)

ax1 =plt.subplot(1,2,1)
ax1.plot(inputVal, cubed, marker='D',c="red",lw="0.2",ls="--")
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()

ax2 =plt.subplot(1,2,2)
ax2.plot(inputVal,squared,marker ="*",c="orange", lw="0.5", ls="--")
plt.title("Square Numbers")
plt.ylabel("Values Squared")
plt.xlabel("Input Values")
plt.grid()
plt.show()