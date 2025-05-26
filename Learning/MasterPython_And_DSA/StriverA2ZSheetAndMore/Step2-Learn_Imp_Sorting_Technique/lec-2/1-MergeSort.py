# Solution 1 :- Naive Solutions
'''
TC:- O((n+m)*log(m+n))
Aux Space: O(n+m)
'''
# def MergeNaive(arr,brr, m, n):
#     c = [0]*(m+n)
#     for i in range(n):
#         c[i] = arr[i]
#     for i in range(m):
#         c[n+i] = brr[i]
#     c = sorted(c)
#     for i in range(m+n):
#         print(c[i],end=' ')

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# brr = list(map(int,input().split()))
# MergeNaive(arr,brr,m,n)


# Solution 2  Efficient Solution

'''
TC:- theta(m+n)
AS:- theta(1)
'''
# def mergeEff(arr,brr,n,m):
#     i,j = 0,0
#     while i<m and j<n:
#         if arr[i] <= brr[j]:
#             print(arr[i], end=' ')
#             i += 1
#         else:
#             print(brr[j],end=' ')
#             j += 1
#     while i<m:
#         print(arr[i],end=' ')
#         i += 1
#     while j<n:
#         print(arr[j],end=' ')
#         j += 1
    

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# brr = list(map(int,input().split()))
# mergeEff(arr,brr,m,n)



'''
Merge Function of Merge Sort

TC:- Theta(n)
AS: Theta(n)
'''

def mergeStandard(arr, low, mid, high):
    # setting of Auxiliary arrays
    n1,n2 = mid-low+1, high-mid
    left = [0]*n1 
    right = [0]*n2 
    for i in range(n1):
        left[i] = arr[low+i]
    for i in range(n2):
        right[i] = arr[mid+i+1]

    # Standard merge Logic
    i,j,k = 0,0,low 
    while i<n1 and j<n2:
        if left[i] <= right[j]:
            arr[k] =  left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i<n1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j<n2:
        arr[k] = right[j]
        k += 1
        j += 1

def mergeSort(arr,l,r):
    if r>l:
        m = l + (r-l)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        mergeStandard(arr,l,m,r)


arr = list(map(int, input().split()))
n = len(arr)
low = 0
mid = n // 2 - 1
high = n - 1

mergeSort(arr, low, high)
print(*arr)