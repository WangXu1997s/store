# i=1
# while i<=9:
#     j=1
#     while(j<=i):
#         print(f'{i}*{j}={i*j}',end='\t')
#         j+=1
#     print('')
#     i+=1
# whlie语法

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={i*j}',end='\t')
#     print()
# for语法

# i=1
# while i<=9:
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end="\t")
#     i+=1
#     print()
# 使用while-for

# for i in range(1,10):
#     j=0
#     while j<i:
#         j+=1
#         print(f'{i}*{j}={i*j}',end='\t')
#     print()
# 使用for-while

# a=[1,2,3,4,5,6,7,8,9]
# for i in a:
#     j=1
#     while j<=i:
#         print(f'{i}*{j}={i*j}',end='\t')
#         j+=1
#     print()
# 定义一个变量a

# def multiplication(n):
#     if n<10:
#         for m in range(1,n+1):
#             print(f'{m}*{n}={m*n}',end='\t')
#         print()
#         multiplication(n+1)
#
# multiplication(1)
# 使用递归

# print('\n'.join([' '.join(["%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

# print('\n'.join([' '.join([f'{j}x{i}={j*i}'for j in range(1,i+1)])for i in range(1,10)]))
# 使用一行语句

# for rowl in range(1,10):
#     for coli in range(rowl,10):
#         print('{0}*{1}={2:2d}'.format(rowl,coli,rowl*coli),end='\t')
#     print()
# 左上角九九乘法表

# for row2 in range(9,0,-1):
#     for block2 in range(9,row2,-1):
#         print(end='\t')
#     for col2 in range(row2,0,-1):
#         print("{0}*{1}={2:2d}".format(row2,col2,row2*col2),end='\t')
#     print()
# 倒三角九九乘法表

# for row2 in range(9,0,-1):
#     for block2 in range(9,row2,-1):
#         print(end='        ')
#     for col2 in range(row2,0,-1):
#         print("{0}*{1}={2:2d}".format(row2,col2,row2*col2),end='\t')
#     print()
# 右上角九九乘法表

# for row3 in range(9,0,-1):
#     for block3 in range(0,row3-1):
#         print(end='        ')
#         # 上面的这个循环for打印出空格，控制乘法表格式
#         # row3虚幻到第几行打印第row3-1空格
#     for col3 in range(9,row3-1,-1):
#         print('{0}*{1}={2:2d}'.format(row3,col3,row3*col3),end='\t')
#     # 这里是用format函数进行格式化输出控制，{2：2d}是给{2}这个位置两倍的控件，对其乘法表
#     # 同时end是print函数内置方法，设置end=“print就不会进行换行操作
#     print()
# 右下角九九乘法表