'''
Naive Partition
AN element that are less than or equal to the pivot must come before it and also that are greater must come after the pivot 
There are many possible output


TC:- O(N)  // but doing three traversal of input array
Aux Spc:- O(N)

'''


# def partition(arr, l, h, p):
#     temp = [0]*(h-l+1)
#     index = 0
#     pivot = arr[p]
#     for i in range(l,h+1):
#         if arr[i]<=pivot:
#             temp[index] = arr[i]
#             index +=1 
#     for i in range(l,h+1):
#         if arr[i]>pivot:
#             temp[index] = arr[i]
#             index += 1
#     for i in range(len(temp)):
#         arr[i] = temp[i]
#     return arr
    


# l = 0
# arr = list(map(int,input("Enter array: ").split()))
# h = len(arr)-1
# p = int(input("Enter pivot index: "))

# arrp = partition(arr,l,h,p)
# print(*arrp)



'''
lOMUTO pARTITION

 Pivot element is always given as input in naive partition but in this pivot we assume always as last element 

 TC:- O(n)  // 1 traversal
 AS:- O(1)
'''

# def lPartition(arr, l, h):
#     pivot = arr[h]
#     i = l - 1
#     for j in range(l, h):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[h] = arr[h], arr[i + 1]
#     return i + 1  # Index of pivot after partitioning

# # Input
# arr = list(map(int, input("Enter array: ").split()))
# l = 0
# h = len(arr) - 1
# p = int(input("Enter pivot index: "))

# # Move pivot to the end for Lomuto partitioning
# arr[p], arr[h] = arr[h], arr[p]

# # Partition the array
# pivot_index = lPartition(arr, l, h)

# # Output
# print("Array after partitioning:")
# print(*arr)
# print("Pivot index after partitioning:", pivot_index)



'''
Hoore's partition
It works much better than lomuto partition method like lomuto partition method, this is also 
O{1} -> Extra space and
O(N) -> Time complexity (1st traversal of i/p array)
- In this we consider 1st element as pivot element

TC:- O(N) // 1 traversal
AS:- O(1)
'''

# def hPartition(arr, l,h):
#     pivot = arr[l] 
#     i = l-1
#     j = h+1

#     while True: 
#         i += 1
#         while arr[i]<pivot:
#             i += 1
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1

#         if i>=j:
#             return j 
#         arr[i], arr[j] = arr[j], arr[i]



# # Input
# arr = list(map(int, input("Enter array: ").split()))
# l = 0
# h = len(arr) - 1
# # Partition the array
# partition_index = hPartition(arr, l, h)


# # Output
# print("Array after partitioning:")
# print(*arr)
# print("Partition index:", partition_index)


'''
- Lomuto and hoore's are not stable algorithm butnaive are stable algorithm
- Hoare's Partition Algorithm is generally faster than Lomuto's because it performs fewer swaps and makes only one traversal of the array, leading to better time complexity in practice.
- It works in-place and does not require extra space, unlike the naive partitioning method which uses a temporary array.
- It can be used to implement a stable version of Quick Sort with the right adjustments, though it is not inherently stable.
- We can easily modify the algorithm to consider the first element (or any other element) as pivot by swapping first and last elements and then using the same code.
'''



'''
                        Quick Sort


- Divide and Conquer Algorithm
- Worst case time: O(n^2)
- Despite  O(N^2) worst case , it is considered faster, cuz of the following reason:-
    - In-Place
    - Cache friendly
    - Average case is O(NlogN)
    - Tail Recursive
- Partition is key function (Naive:- Stable, Lomuto & Hoore's :- Non_stable)

- Naive partition is generally not used
- Lomuto & Hoore partition are preferred among this two Hoore's is the most efficient algorithm
- With Hoore's is th emost efficient partitioning
- With Hoore's we get a fast sorting algorithm but this is not stable
- Many library implementation do quick sort when stability is not required

- In C++, there are two factor:-
    1. Sort : Uses quick sort internally
    2. Stable sort

- C library has a function called qsort(), as the name suggest Quick SOrt implementation
- Java uses Quick Sort for primitive data type sorting
- For non-primitive data types, Java uses Timsort is a variation of Merge sort
- Python and Java uses non-primitive type sorting based on Merge Sort they are stable 

Q) Compare Merge Sort with Quick Sort?
- When we don't need stability then quick sort is definetly the fastest algorithm, Quick sort or its variation intro sort version, they are the fastest variation actually use in library also.

- If we need stability also then merge sort is preferred
'''






# ##############   Quick Sort using Lomuto Partition



# def lPartition(arr, l, h):
#     pivot = arr[h]
#     i = l - 1
#     for j in range(l, h):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[h] = arr[h], arr[i + 1]
#     return i + 1  # Index of pivot after partitioning


# def qSort(arr,l,h):
#     if l<h:
#         p = lPartition(arr,l,h)
#         qSort(arr,l,p-1)
#         qSort(arr,p+1,h)
#     return arr


# # Input
# arr = list(map(int, input("Enter array: ").split()))
# l = 0
# h = len(arr) - 1
# p = int(input("Enter pivot index: "))

# # Move pivot to the end for Lomuto partitioning
# arr[p], arr[h] = arr[h], arr[p]

# # Partition the array
# arrp= qSort(arr, l, h)

# # Output
# print("Array after partitioning:")
# print(*arrp)





#######   Quick Sort using Hoore's Partition    ######


def hPartition(arr, l,h):
    pivot = arr[l] 
    i = l-1
    j = h+1

    while True: 
        i += 1
        while arr[i]<pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i>=j:
            return j 
        arr[i], arr[j] = arr[j], arr[i]

def hSort(arr,l, h):
    if l<h:
        p = hPartition(arr,l,h)
        hSort(arr,l,p)
        hSort(arr,p+1,h)
    return arr


# Input
arr = list(map(int, input("Enter array: ").split()))
l = 0
h = len(arr) - 1
# Partition the array
arrh = hSort(arr, l, h)


# Output
print("Array after partitioning:")
print(*arrh)


