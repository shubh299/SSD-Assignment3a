def isLeap(year):
    if(year%400==0):
        return True
    if(year%100==0):
        return False
    if(year%4==0):
        return True

def returnDate(date):
    if '/' in date:
        date=date.split('/')
        return int(date[0]),int(date[1]),int(date[2])
    if '-' in date:
        date=date.split('-')
        return int(date[0]),int(date[1]),int(date[2])
    if '.' in date:
        date=date.split('.')
        return int(date[0]),int(date[1]),int(date[2])
        
    year=date[-4:]
    if 'th ' in date:
        seperator='th'
    if 'st ' in date:
        seperator='st'
    if 'nd ' in date:
        seperator='nd'
    if 'rd ' in date:
        seperator='rd'
    
    day=date.split(seperator)[0].strip()
    month=date.split(seperator)[1].strip()[0:3]
    monthDict={'Jan':1,'Feb':2,'Mar':3,'Apr':4,
              'May':5,'Jun':6,'Jul':7,'Aug':8,
              'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    month=monthDict[month]
    return int(day),int(month),int(year)

def findDifference(date1,date2):
    monthDays=[0,31,28,31,30,31,30,31,31,30,31,30]
    monthDaysSum=[0]
    for i in range(1,len(monthDays)):
        monthDaysSum.append(monthDaysSum[i-1]+monthDays[i])
    
    totalDays1=(date1[2])*365
    leapNo1=int(date1[2]//4-date1[2]//100+date1[2]//400)
    totalDays1=totalDays1+leapNo1
    isLeap1=isLeap(date1[2])
    if isLeap1 and date1[1]<2:
        totalDays1=totalDays1-1
    totalDays1=totalDays1+monthDaysSum[date1[1]-1]
    totalDays1=totalDays1+date1[0]
    
    totalDays2=(date2[2])*365
    leapNo2=int(date2[2]//4-date2[2]//100+date2[2]//400)
    totalDays2=totalDays2+leapNo2
    isLeap2=isLeap(date2[2])
    if isLeap1 and date2[1]<2:
        totalDays2=totalDays2-1
    totalDays2=totalDays2+monthDaysSum[date2[1]-1]
    totalDays2=totalDays2+date2[0]
    
    return abs(totalDays2-totalDays1)
    
f=open('date_calculator.txt')
date1=f.readline().strip()[7:]
date2=f.readline().strip()[7:]
f.close()
date1=returnDate(date1)
date2=returnDate(date2)
diff=findDifference(date1,date2)
f=open('output.txt','w')
f.write("Date Difference: "+str(diff)+" Day\n")
f.close()
