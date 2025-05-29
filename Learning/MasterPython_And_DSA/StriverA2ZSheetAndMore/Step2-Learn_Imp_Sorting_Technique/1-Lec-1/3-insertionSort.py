'''
TC:- 
Best Case: Already sorted : theta(n)
Worst Case : reverse Sorted : O(N^2)
In general : O(N^2)
'''

def insertionSort(arr,n):
    for i in range(n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 
    return arr 

n = int(input())
arr = list(map(int, input().split()))

print(*insertionSort(arr,n))

