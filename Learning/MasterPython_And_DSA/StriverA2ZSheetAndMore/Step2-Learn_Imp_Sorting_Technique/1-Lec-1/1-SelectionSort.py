# Solution 1  Naive 

'''
TC:- O(N^2)
'''

import math
def selectionSort(arr,n):
    temp = []
    for i in range(n):
        mini_ind = -1
        for j in range(n):
            if arr[j] < arr[mini_ind]:
                mini_ind = j 
        temp.append(arr[mini_ind])
        arr[mini_ind] = math.inf 

    for i in range(n):
        arr[i] = temp[i]


n=int(input())
arr = list(map(int,input().split()))
selectionSort(arr,n)
print(*arr)


# Solution 2 Naive

import math

def selectionSort(arr, n):
    temp = []
    for i in range(n):
        mini_ind = -1
        for j in range(n):
            if arr[j] != math.inf:
                if mini_ind == -1 or arr[j] < arr[mini_ind]:
                    mini_ind = j
        temp.append(arr[mini_ind])
        arr[mini_ind] = math.inf

    for i in range(n):
        arr[i] = temp[i]

# Input section
n = int(input())
arr = list(map(int, input().split()))
selectionSort(arr, n)

# Output (for verification)
print(*arr)


# Solution 3 Inplace Implementation



def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print_array(arr)