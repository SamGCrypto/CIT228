import csv
import matplotlib.pyplot as plt
filename="NCHS_BIRTH_DEATH_2000s.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row_birth = next(reader)

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
    total11 = 0
    total12 = 0
    total13 = 0
    total14 = 0
    total15 = 0
    total16 = 0
    total17 = 0
    total18 = 0
    for row in reader:
        if(int(row[0])==2000):
            total00=float(row[3])
        if(int(row[0])==2001):
            total01=float(row[3])
        if(int(row[0])==2002):
            total02=float(row[3])
        if(int(row[0])==2003):
            total03=float(row[3])
        if(int(row[0])==2004):
            total04=float(row[3])
        if(int(row[0])==2005):
            total05=float(row[3])
        if(int(row[0])==2006):
            total06=float(row[3])
        if(int(row[0])==2007):
            total07=float(row[3])
        if(int(row[0])==2008):
            total08=float(row[3])
        if(int(row[0])==2009):
            total09=float(row[3])
        if(int(row[0])==2010):
            total10=float(row[3])
        if(int(row[0])==2011):
            total11=float(row[3])
        if(int(row[0])==2012):
            total12=float(row[3])
        if(int(row[0])==2013):
            total13=float(row[3])
        if(int(row[0])==2014):
            total14=float(row[3])
        if(int(row[0])==2015):
            total15=float(row[3])
        if(int(row[0])==2016):
            total16=float(row[3])
        if(int(row[0])==2017):
            total17=float(row[3])
        if(int(row[0])==2018):
            total18=float(row[3])

    totals=[]
    totals.append(total00)
    totals.append(total01)
    totals.append(total02)
    totals.append(total03)
    totals.append(total04)
    totals.append(total05)
    totals.append(total06)
    totals.append(total07)
    totals.append(total08)
    totals.append(total09)
    totals.append(total10)    
    totals.append(total11)
    totals.append(total12)
    totals.append(total13) 
    totals.append(total14) 
    totals.append(total15)
    totals.append(total16) 
    totals.append(total17)
    totals.append(total18)        
    years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
    print(totals)

    ax=plt.subplot()
    ax.scatter(years, totals, c=totals, cmap=plt.cm.viridis,s=150)
    plt.ylabel("Life Expenctancy")
    plt.xlabel("Years")
    plt.title("Life expenctancy")
    plt.legend(loc='lower center',ncol=30,fontsize=8)

    plt.show()
