def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[5,2,4,7,9,1,3,5,4,0,6,1,3]
bubbleSort(arr)
print(arr)