a=[1,5,21,30,15,9,30,24]
b=0
sum=0
for i in range(0,len(a)):
    if a[i]%5==0:
        b=a[i]
        sum+=b

print(sum)
        