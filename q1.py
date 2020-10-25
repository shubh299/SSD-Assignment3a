import json

f=open('org.json',)
data=json.load(f)
f.close()

orgDict=dict()

top=data['L0'][0]['name']

for value in data.values():
    for i in value:
        if 'parent' in i:
            orgDict[i['name']]=i['parent']

emp1=input()
emp2=input()

emp1Leaders=list()
emp2Leaders=list()
if emp1==top or emp2==top:
    print("Leader not found")
    exit()
parent=orgDict[emp1]
emp1Leaders.append(parent)
while parent!=top:
    parent=orgDict[parent]
    emp1Leaders.append(parent)
parent=orgDict[emp2]
emp2Leaders.append(parent)
while parent!=top:
    parent=orgDict[parent]
    emp2Leaders.append(parent)

leader='000'
pos1=-1
pos2=-1
for i in emp1Leaders:
    pos1=pos1+1
    if i in emp2Leaders:
        leader=i
        pos2=emp2Leaders.index(i)
        break
if i!='000':
    print(i,"is common leader of employee",emp1,"and employee",emp2)
    print("leader",i,"is",pos1+1,"levels above",emp1)
    print("leader",i,"is",pos2+1,"levels above",emp2)
