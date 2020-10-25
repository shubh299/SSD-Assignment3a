import json
import datetime

class Employee:
    empFreeSlots=list()
    def __init__(self,name,date,busySlots):
        self.name=name
        self.date=date
        self.busySlots=busySlots
    
    def findFreeSlots(self,start,end):
        self.freeSlots=list()
        slotStart=start
        slotEnd=""
        index=0
        if start in self.busySlots[0]:
            index=1
            slotStart=self.busySlots[0].split('-')[1].strip()
        while index<len(self.busySlots):
            slotEnd=self.busySlots[index].split('-')[0].strip()
            slot=slotStart+' - '+slotEnd
            if slotStart!=slotEnd:
                self.freeSlots.append(slot)
            slotStart=self.busySlots[index].split('-')[1].strip()
            index=index+1
        if slotStart!=end:
            slot=slotStart+' - '+end
            self.freeSlots.append(slot)
            
            
start='9:00AM'
end='5:00PM'

f=open('Employee1.txt')
emp1=f.readline()
f.close()
emp1=json.loads(emp1.strip().replace("'","\""))
emp1Slots=list(emp1.values())[0]
employee1=Employee(list(emp1.keys())[0],list(emp1Slots.keys())[0],list(emp1Slots.values())[0])
employee1.findFreeSlots(start,end)

f=open('Employee2.txt')
emp2=f.readline()
f.close()
emp2=json.loads(emp2.strip().replace("'","\""))
emp2Slots=list(emp2.values())[0]
employee2=Employee(list(emp2.keys())[0],list(emp2Slots.keys())[0],list(emp2Slots.values())[0])
employee2.findFreeSlots(start,end)

f=open("output.txt",'w')
f.write("Available Slot\n")
f.write(employee1.name+':'+str(employee1.freeSlots)+'\n')
f.write(employee2.name+':'+str(employee2.freeSlots)+'\n')
slotDuration=float(input())
if employee1.date!=employee2.date:
	f.write("No slot available\n")
else:
	commonSlots=list()
	for interval1 in employee1.freeSlots:
		for interval2 in employee2.freeSlots:
		    t11,t12=interval1.split('-')
		    t21,t22=interval2.split('-')
		    t11=datetime.datetime.strptime(t11.strip(),"%I:%M%p")
		    t12=datetime.datetime.strptime(t12.strip(),"%I:%M%p")
		    t21=datetime.datetime.strptime(t21.strip(),"%I:%M%p")
		    t22=datetime.datetime.strptime(t22.strip(),"%I:%M%p")
		    t1=max(t11,t21)
		    t2=min(t12,t22)
		    if(t1>=t2):
		        continue
		    commonSlots.append((t1,t2))
	commonSlot=tuple()
	for i in commonSlots:
		if slotDuration*60<=(i[1]-i[0]).seconds//60:
		    commonSlot=(i[0],i[0]+datetime.timedelta(minutes=slotDuration*60))
		    break
	if commonSlot==():
		f.write("No slot available\n")
	else:
		slotDict={employee1.date:[datetime.datetime.strftime(commonSlot[0],"%I:%M%p")+" - "+datetime.datetime.strftime(commonSlot[1],"%I:%M%p")]}
		f.write("Slot Duration: "+str(slotDuration)+" hour\n")
		f.write(str(slotDict)+"\n")
f.close()
