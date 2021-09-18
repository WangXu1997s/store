# 正三角形
# for i in range(10):
#     for j in range(0,10-i):
#         print(end=' ')
#     for k in range(10-i,10):
#         print('*',end=" ")
#
#     print("")
#
#
# 倒三角形
# for i in range(10):
#     for j in range(0,i):
#         print(end=" ")
#     for k in range(i,10):
#         print('*',end=" ")
#
#     print("")


# 左上角三角形
# for i in range(10):
#     for j in range(0,10-i):
#         print("*",end=" ")
#
#     print("")


# 左下角三角形
# for i in range(10):
#     for j in range(0,i):
#         print("*",end=" ")
#     print('')


# 右上角三角形
# for i in range(10):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for k in range(i,10):
#         print("*",end=' ')
#     print('')


# 右下角三角形
# for i in range(10):
#     for j in range(0,10-i):
#         print(" ",end=" ")
#     for k in range(10-i,10):
#         print("*",end=" ")
#     print("")

# 杨辉三角形
# def triangle():
#     N=[1]
#     while True:
#           yield N   # generator特点在于：在执行过程中，遇到yield就中断，下次又继续执行
#           L=N.copy()  # 我们需要把N复制给L，而不能直接L=N，因为这样L和N会在同一个地址，后续算法就会出错
#           for j in range(len(L)): #遍历和转化
#               temp=str(L[j])
#               L[j]=temp
#           l=" ".join(L).center(50) # 组合和居中一起写
#           print(l) # 这里就是打印L了
#           N.append(0) # 每次都要在最后一位加个0，用于后续的叠加
#           N=[N[i]+N[i-1]for i in range(len(N))]
#
# def print_triangle(x):
#     a=0
#     for t in triangle(): # 这里可以每次调用一个N（得力于yield函数）
#         # print(t)
#         a+=1
#         if a==x:
#             break
#
# print_triangle(10)