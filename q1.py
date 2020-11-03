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

input_emp=input().split(' ')
number_of_employees=int(input_emp[0])
employee_list=input_emp[1:]

if top in employee_list:
    print("Leader not found")
    exit()

leaders_list=list()
for emp in employee_list:
    parent=orgDict[emp]
    temp_list=list()
    temp_list.append(parent)
    while parent!=top:
        parent=orgDict[parent]
        temp_list.append(parent)
    leaders_list.append(temp_list)

leader='000'

for i in leaders_list[0]:
    count=0
    for list_index in range(1,number_of_employees):     
        if i in leaders_list[list_index]:
            count+=1
    if count==number_of_employees-1:
        leader=i
        break

if leader!='000':
    print("Common leader:",leader)
    for list_index in range(0,len(leaders_list)):
        print("leader",leader,"is",leaders_list[list_index].index(leader)+1,"levels above",employee_list[list_index])
