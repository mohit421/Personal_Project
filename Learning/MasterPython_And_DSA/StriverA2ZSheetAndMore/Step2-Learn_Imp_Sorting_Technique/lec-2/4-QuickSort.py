'''
Naive Partition
'''


def partition(arr, l, h, p):
    temp = [0]*(h-l+1)
    index = 0
    for i in range(l,h+1):
        if arr[i]<arr[p]:
            temp[index] = arr[i]
            index +=1 
    for i in range(l,h+1):
        if arr[i]>arr[p]:
            temp[index] = arr[i]
            index += 1
    for i in range(l,h+1):
        arr[i] = temp[i-l]
    


l = 0
arr = list(map(int,input().split()))
h = len(arr)-1
p = int(input())

arrp = partition(arr,l,h,p)
print(*arrp)


