import time
from threading import Thread
eggtarts=500
money=3000
class cook(Thread):
    def run(self) -> None:
        global eggtarts
        global money
        while True:
            if eggtarts<500:
                eggtarts+=1
            elif eggtarts==500:
                time.sleep(3)
                if money<2:
                    break



class customer(Thread):
    username=''
    count=0
    def run(self) -> None:
        global eggtarts
        global money
        while True:
            if money>=2:
                if eggtarts>0 :
                    eggtarts-=1
                    money-=2
                    self.count+=1
                    print(self.username,'成功抢到了蛋挞','还剩',eggtarts,'个')
                elif eggtarts==0:
                    time.sleep(3)
            else:
                print(self.username,'抢到了',self.count,'个蛋挞')
                break

c0=cook()
c1=cook()
c2=cook()
n0=customer()
n1=customer()
n2=customer()
n3=customer()
n4=customer()
n5=customer()
n0.username='甲'
n1.username='乙'
n2.username='丙'
n3.username='丁'
n4.username='戊'
n5.username='己'
c0.start()
c1.start()
c2.start()
n0.start()
n1.start()
n2.start()
n3.start()
n4.start()
n5.start()
