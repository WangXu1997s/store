info = {
    '苹果':32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
dict={}
dict['苹果']=32.8
dict['香蕉']=22
dict['葡萄']=15.5


Friuts = {
	'苹果':12.3,  # 水果和单价
	'草莓':4.5,
       '香蕉':6.3,
       '葡萄':5.8,
       '橘子':6.4,
       '樱桃':15.8
}
info2= {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},

    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},

    }
}


info2['小明']['money']=Friuts['草莓']*info2['小明']["fruits"]['草莓']+Friuts['香蕉']*info2['小明']["fruits"]['香蕉']+Friuts['苹果']*info2['小明']["fruits"]['苹果']

info2['小刚']['money']=Friuts['葡萄']*info2['小刚']['fruits']['葡萄']+Friuts['橘子']*info2['小刚']['fruits']['橘子']+Friuts['樱桃']*info2['小刚']['fruits']['樱桃']

print(info2)