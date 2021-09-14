# 猜字游戏
# 需求：
# 1、猜的数字是系统产生的，不是自己定义的
# 2、键盘输入的   操作完填入：input（“提示”）
# 3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
# 4、循环			操作完填入：while 条件循环
#任务  判断如果你输入的数字大于随机生成的数字那么给一个提示你猜大了
#                      小于                         小了
#起始资充钱 1000  （账户原有资金+刚充值的资金）10%  2000 20%   每猜一次-500一直执行
#游戏开始按1   退出游戏Q
#资金为0 锁死系统
#5次猜对，5次机会用光了就退出
zijin = int(input("请输入充值金额："))
yue = 0
n=5

while True :
    if zijin%1000!=0:
        print("请输入1000的整数倍")
        zijin=int(input("请再次输入充值金额："))

    elif zijin==0:
        if num=="1":
            import  random
            ran=random.randint(0,90)

            while True:

                fuzhi = int(input("请输入一个数字："))
                if fuzhi==ran :
                    print("ok")
                elif fuzhi>=ran:
                    print("您输大了")
                    n=n-1
                    yue=yue-500
                    if n==0:
                        num = input("您已用完五次机会，输入1游戏重新开始，输入q退出游戏：")
                        zijin = int(input("充值请输入充值金额，如不需要请输入0："))
                        n=5
                        break
                    else:
                        if yue<500:
                            zijin = int(input("资金不足请充值："))
                            break

                elif fuzhi<=ran:
                    print("您输小了")
                    n=n-1
                    yue=yue-500
                    if n==0:
                        num=input("您已用完五次机会，输入1游戏重新开始，输入q退出游戏：")
                        zijin=int(input("充值请输入充值金额，如不需要请输入0："))
                        n=5
                        break
                    else:
                        if yue<500:
                            zijin=int(input("资金不足请充值："))
                            break

        elif num=="q":
            break
        else:
            num=input("输入1游戏开始，输入q退出游戏")
    else:
        yue = yue+zijin + zijin * zijin / 10000
        print("充值成功，您的余额为：",yue)
        num=input("输入1游戏开始，输入q退出游戏")
        if num=="1":
            import  random
            ran=random.randint(0,90)

            while True:

                fuzhi = int(input("请输入一个数字："))
                if fuzhi==ran :
                    print("ok")
                elif fuzhi>=ran:
                    print("您输大了")
                    n=n-1
                    yue=yue-500
                    if n==0:
                        num = input("您已用完五次机会，输入1游戏重新开始，输入q退出游戏：")
                        zijin = int(input("充值请输入充值金额，如不需要请输入0："))
                        n=5
                        break
                    else:
                        if yue<500:
                            zijin = int(input("资金不足请充值："))
                            break

                elif fuzhi<=ran:
                    print("您输小了")
                    n=n-1
                    yue=yue-500
                    if n==0:
                        num=input("您已用完五次机会，输入1游戏重新开始，输入q退出游戏：")
                        zijin=int(input("充值请输入冲击金额，如不需要请输入0："))
                        n=5
                        break
                    else:
                        if yue<500:
                            zijin=int(input("资金不足请充值："))
                            break

        elif num=="q":
            break
        else:
            num=input("输入1游戏开始，输入q退出游戏")






