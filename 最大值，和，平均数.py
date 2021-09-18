max=0
sum=0
avg=0
for num in range(10):
    a=int(input("请输入第{}个数：".format(num+1)))
    sum+=a
    avg=sum/10
    if a>max:
        max=a

print("最大值为：",max)
print("和为：",sum)
print("平均数为：",avg)