a,b,c=map(int,input().split())
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('构成等边三角形')
    elif a==b or a==c or b==c:
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print('构成等腰直角三角形')
        else:
            print('构成等腰三角形')
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print('构成直角三角形')
    else:
        print('构成普通三角形')
else:
    print('无法构成三角形')