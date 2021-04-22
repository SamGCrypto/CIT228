import csv
import matplotlib.pyplot as plt
filename="NCHS_BIRTH_DEATH_2000s.csv"

filenameBirth="US_births_2000-2014_SSA.csv"
with open(filenameBirth) as b:
    reader=csv.reader(b)
    header_row_birth = next(reader)


with open(filename) as f:
    reader=csv.reader(f)
    header_row = next(reader)
    
    death = []
    total00 = 0
    total01 = 0
    total02 = 0
    total03 = 0
    total04 = 0
    total05 = 0
    total06 = 0
    total07 = 0
    total08 = 0
    total09 = 0
    total10 = 0
    for row in reader:
        if(int(row[0])==2000):
            total00+=(float(row[4])*10)
        if(int(row[0])==2001):
            total01+=(float(row[4])*10)
        if(int(row[0])==2002):
            total02+=(float(row[4])*10)
        if(int(row[0])==2003):
            total03+=(float(row[4])*10)
        if(int(row[0])==2004):
            total04+=(float(row[4])*10)
        if(int(row[0])==2005):
            total05+=(float(row[4])*10)
        if(int(row[0])==2006):
            total06+=(float(row[4])*10)
        if(int(row[0])==2007):
            total07+=(float(row[4])*10)
        if(int(row[0])==2008):
            total08+=(float(row[4])*10)
        if(int(row[0])==2009):
            total09+=(float(row[4])*10)
        if(int(row[0])==2010):
            total10+=(float(row[4])*10)


    totalsDeath=[]
    totalsDeath.append(total00)
    totalsDeath.append(total01)
    totalsDeath.append(total02)
    totalsDeath.append(total03)
    totalsDeath.append(total04)
    totalsDeath.append(total05)
    totalsDeath.append(total06)
    totalsDeath.append(total07)
    totalsDeath.append(total08)
    totalsDeath.append(total09)
    totalsDeath.append(total10)    
    years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

filename="US_births_2000-2014_SSA.csv"
with open(filename) as f:
    readerBirth=csv.reader(f)
    header_row = next(readerBirth)
    
    births = []
    total00 = 0
    total01 = 0
    total02 = 0
    total03 = 0
    total04 = 0
    total05 = 0
    total06 = 0
    total07 = 0
    total08 = 0
    total09 = 0
    total10 = 0
    counter0=0
    counter1=0
    counter2=0
    counter3=0
    counter4=0
    counter5=0
    counter6=0
    counter7=0
    counter8=0
    counter9=0
    counter10=0
    for row in readerBirth:
        if(int(row[0])==2000):
            total00+=int(row[4])
            counter0 +=1
        if(int(row[0])==2001):
            total01+=int(row[4])
            counter1 +=1
        if(int(row[0])==2002):
            total02+=int(row[4])
            counter2 +=1
        if(int(row[0])==2003):
            total03+=int(row[4])
            counter3 +=1
        if(int(row[0])==2004):
            total04+=int(row[4])
            counter4 +=1
        if(int(row[0])==2005):
            total05+=int(row[4])
            counter5 +=1
        if(int(row[0])==2006):
            total06+=int(row[4])
            counter6 +=1
        if(int(row[0])==2007):
            total07+=int(row[4])
            counter7 +=1
        if(int(row[0])==2008):
            total08+=int(row[4])
            counter8 +=1
        if(int(row[0])==2009):
            total09+=int(row[4])
            counter9 +=1
        if(int(row[0])==2010):
            total10+=int(row[4])
            counter10 +=1

    
    totals=[]
    totals.append(total00/counter0)
    totals.append(total01/counter1)
    totals.append(total02/counter2)
    totals.append(total03/counter3)
    totals.append(total04/counter4)
    totals.append(total05/counter5)
    totals.append(total06/counter6)
    totals.append(total07/counter7)
    totals.append(total08/counter8)
    totals.append(total09/counter9)
    totals.append(total10/counter10)


plt.suptitle("Births and Deaths for 2000-2010")
plt.subplots_adjust(top=.8,wspace=1)

ax2 = plt.subplot(1,2,1)
ax2.plot(years, totalsDeath,c="purple")
plt.title("Deaths")
plt.grid()


ax1 = plt.subplot(1,2,2)
ax1.plot(years, totals,c="purple")
plt.title("Births")
plt.grid()

plt.show()
