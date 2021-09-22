names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
# 统计每个人的平均薪资
for i in range(0,len(names)):

    print(names[i][0],'平均工资为',names[i][5],'平均年龄为',names[i][1])

names.append(['刘备','45','男','220','alibaba',500,'30'])
print(names)

n=0
m=0
for i in range(0,len(names)):
    if names[i][2]=='男':
        n+=1
    if names[i][2]=='女':
        m+=1
print('男的有',n,'女的有',m)

a=0
b=0
c=0
d=0
for i in range(0,len(names)):
    if names[i][6]=='50':
        a+=1
    if names[i][6]=='60':
        b+=1
    if names[i][6]=="30":
        c+=1
    if names[i][6]=='10':
        d+=1
print('50部门有',a,'60部门有',b,'30部门有',c,'10部门有',d)

