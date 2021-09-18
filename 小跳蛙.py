a=20
b=0
num=0
while True :
    if b<a:
        b+=3
        num+=1
        if b<a:
            b-=2
        else:
            print("第",num,'天能跳出来')
            break
    else:
        print("第", num, '天能跳出来')
        break
