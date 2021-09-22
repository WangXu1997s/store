score=[
['罗恩',23,35,44],
['哈利',60,77,68,88,90],
['赫敏',97,99,89,91,95,90],
['马尔福',100,85,90]
]

for i in range(len(score)):
    sum = 0
    for j in range(1,len(score[i])):
        sum=score[i][j]+sum
    print(score[i][0],'的总成绩为',sum)
