
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
setL = set(List)
#print(setL.pop())
for i in range(len(setL)):
    view = setL.pop()
    print("{0}出现了{1}次。".format(view,List.count(view)))