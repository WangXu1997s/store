class oldphone:
    __brand=''

    def setbrand(self,brand):
        self.__brand=brand

    def getbrand(self):
        return self.__brand

    def call(self,number):
        print('正在给',number,'打电话')

class newphone(oldphone):

    def call(self,number):
        print('正在通话中……')
        super().call(number)

    def good(self,brand):

        print('品牌为',brand,'的手机很好用')

p=newphone()

p.call(19943451560)
p.good('华为')


class cook:
    __name=''
    __age=0
    def setname(self,name):
        self.__name=name
        print(self.__name)
    def setage(self,age):
        self.__age=age
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def zhengfan(self):
        return
class cook1(cook):
    def cooking(self):
        return
class cook2(cook1):
    def zhengfan(self,food):
        print('正在',food)
    def cooking(self,foodds):
        print('正在炒',foodds)
class cook3(cook2):
    pass

h=cook3()
h.setage(10)
h.setname('wabg')

class person:
    __name=''
    __age=0
    __gender=''
    def setname(self,name):
        self.__name=name
    def setage(self,age):
        self.__age=age
    def setgender(self,gender):
        self.__gender=gender
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def getgender(self):
        return self.__gender

class worker(person):
    def working(self,what):
        return
class student(person):
    __studentId=0
    def set(self,id):
        self.__studentId=id
    def get(self):
        return self.__studentId
    def sing(self,ge):
        print('正在唱',ge)
    def studing(self,hour):
        print('学了',hour,'个小时了')