import json
import  time
from datetime import datetime

def utilize():
    data=[
        {'usr':'sty','pwd':'123','lock':0,'cnt':0,'time':'2021-09-15 20:28:00'},
        {'usr':'bat','pwd':'alibaba','lock':0,'cnt':0,'time':'2021-09-15 20:28:00'}
    ]

    with open('data.json','w') as f:
        json.dump(data,f)

# 判断间隔时间
def time_judge(start_time,end_time):
    day=(end_time - start_time).days
    return day

# 本地时间转UTC时间（-8:00）
def local2utc(local_st):
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.utcfromtimestamp(time_struct)
    return utc_st

# login判断登录
def login():
    with open('data.json','r') as f:
        res = json.load(f)
    while Ture:
        new=[]
        user_name = input('user_name:')
        user_pwd=input('user_pwd:')
        flag=0
        # flag:0表示该用户不存在；1表示用户存在密码正确；2表示用户名存在，但是被锁定或密码错误
        for user in res:
            if user['usr']==user_name:
                flag=2
                last_time=datetime.strptime(user['time'],'%Y-%m-%d %H:%M:%S')
                now_time=utc2local(datetime.utcnow())
                # 判断时间间隔
                if time_judge(last_time,now_time)>1:
                    user['lock']=0
                    user['cnt']=0
                if user['pwd'] == user_pwd:
                    if user['lock'] == 1:
                        print('you have been locked ')
                    else:
                        flag = 1
                        user['cnt'] = 0
                        print("welcome to file")
                else:
                    if user['lock'] == 1:
                        print('you have been locked ')
                    else:
                        user['cnt'] = user['cnt'] + 1
                        # 如果user输入密码三次锁定用户
                        if user['cnt'] == 3:
                            user['lock'] = 1

                user['time'] = now_time.strftime("%Y- %m- %d %H:%M:%S")  # 更新登录时间
            new. append(user)

        # 文件中更新帐户数据
        # print(new)
        with open('data.json','w') as f:
            json.dump(new,f)
        if flag==1:
            break
        if flag==0:
            print("this user is not exist")

