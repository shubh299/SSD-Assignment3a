import json
import datetime
import os

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

employee_list=list()
dir_path="input_files/"
for file in os.listdir(dir_path):
    f=open("input_files/"+file)
    emp=f.readline()
    f.close()
    emp=json.loads(emp.strip().replace("'","\""))
    empSlots=list(emp.values())[0]
    employee=Employee(list(emp.keys())[0],list(empSlots.keys())[0],list(empSlots.values())[0])
    employee.findFreeSlots(start,end)
    employee_list.append(employee)

f=open("output.txt",'w')
f.write("Available Slot\n")
for emp in employee_list:
    f.write(emp.name+':'+str(emp.freeSlots)+'\n')
slotDuration=float(input())

date_list=[d.date for d in employee_list]
if date_list.count(date_list[0])!=len(date_list):
    print("No slot available\n")

else:
	commonSlots=[(datetime.datetime.strptime(interval.split('-')[0].strip(),"%I:%M%p"),datetime.datetime.strptime(interval.split('-')[1].strip(),"%I:%M%p")) for interval in employee_list[0].freeSlots]
	for i in range(1,len(employee_list)):
		tempSlots=list()
		for interval2 in employee_list[i].freeSlots:
			for interval1 in commonSlots:
				t11=interval1[0]
				t12=interval1[1]
				t21,t22=interval2.split('-')
				t21=datetime.datetime.strptime(t21.strip(),"%I:%M%p")
				t22=datetime.datetime.strptime(t22.strip(),"%I:%M%p")
				t1=max(t11,t21)
				t2=min(t12,t22)
				if(t1>=t2):
					continue
				tempSlots.append((t1,t2))
		commonSlots=tempSlots
	commonSlot=tuple()
	for i in commonSlots:
		if slotDuration*60<=(i[1]-i[0]).seconds//60:
		    commonSlot=(i[0],i[0]+datetime.timedelta(minutes=slotDuration*60))
		    break
	if commonSlot==():
		f.write("No slot available\n")
	else:
		slotDict={date_list[0]:[datetime.datetime.strftime(commonSlot[0],"%I:%M%p")+" - "+datetime.datetime.strftime(commonSlot[1],"%I:%M%p")]}
		f.write("Slot Duration: "+str(slotDuration)+" hour\n")
		f.write(str(slotDict)+"\n")
f.close()
