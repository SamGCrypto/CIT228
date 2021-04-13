import csv
import matplotlib.pyplot as plt
filename="Arctic.csv"
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    highs =[]
    for row in reader:
        if(row[4]!=''):
            high=row[int(4)]
            highs.append(high)

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(highs, c="red")

ax.set_yticklabels([])
ax.set_title("Daily high temperatures in Antarctica, from January to 4/09/2021",fontsize=25)
ax.set_xlabel('',fontsize=12)
ax.set_ylabel("Temperatures (F)",fontsize=12)
ax.tick_params(axis="both",which='major',labelsize=13)

plt.show()