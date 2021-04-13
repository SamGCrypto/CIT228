import matplotlib.pyplot as plt
def autopct_format(values):
    def my_format(pct):
        total=sum(values)
        val=int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format

labels ='PNG','JPEG','SVG','GIF','Other'
usedSites=376,348,153,104,19
explode=(.3,0,0,0,0)
wedgeColors=('red','blue','yellow','purple','orange')

fig1,ax1 = plt.subplots()
ax1.pie(usedSites, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=0, colors=wedgeColors)
ax1.axis('equal')
plt.suptitle("Most popular pets in America")

plt.show()