# Solution 1

# def bubbleSort(arr,n):
#     for i in range(n):
#         for j in range(n-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
# n = int(input())
# arr = list(map(int, input().split()))

# print(*bubbleSort(arr,n))


# Solution 2 Optimized Solution
'''
TC:- theta(n^2)
'''

# def bubbleSort(arr,n):
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr 

# n = int(input())
# arr = list(map(int, input().split()))

# print(*bubbleSort(arr,n))


# Solution 3

# We can optimized the bubble sort when the array is sorted

def bubbleSort(arr,n):
    for i in range(n-1):
        swapped = False 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True 
        if swapped == False:
            break
    return arr 

n = int(input())
arr = list(map(int, input().split()))

print(*bubbleSort(arr,n))

