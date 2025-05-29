'''
- it is our linear time algorithm for the cases when our input elements are in small range
- If we have n element and element are in range from 0 to k-1 then counting sort goinhg to take O(n+k) time
- It is not a comparison based algorithm it never compares items with each other rather it counts the occurences
- It is useful only hwne k is linear in terms of n for eg) n or n/2 or 2n or 3n etc when it becomes quadratic, logarithmic it is of no use.
- Bcuz we have algo, comparison based algorithm that works for any range and take O(NlogN) time
'''

# Naive Implementation

# def countSort(arr, n, k):
#     count = [0]*k 
#     # for i in range(k):
#     #     count[i] = 0
#     for i in range(n):
#         count[arr[i]] += 1
#     idx = 0
#     for i in range(k):
#         for j in range(count[i]):
#             arr[idx] = i 
#             idx += 1



# ---- User input part ----
# # Input format: space-separated integers
# arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
# n = len(arr)
# k = max(arr) + 1  # max element + 1 is the range

# countSort(arr, n, k)

# print("Sorted array:")
# print(*arr)


'''
problem with naive approach
- Can't be used as a general purpose algorithm for sorting objects with multiple members, like sorting an array of students by marks


- General purpose Implementattion
- It works really well , when we have objects to be sorted also and these  objects are to be sorted according to a certain key 
- It works for integer as well

'''


'''
- Not a comparison based algorithm
- theta(n+k) time 
- theta(n+k) auxiliary space
- stab;e
- used as a subroutine in radix sort

'''
def countSort(arr, n, k):
    count = [0] * k

    # Step 1: Count occurrences
    for i in range(n):
        count[arr[i]] += 1

    # Step 2: Update count to store positions
    for i in range(1, k):
        count[i] += count[i - 1]

    # Step 3: Build the output array (stable sort - iterate backwards)
    output = [0] * n
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # Step 4: Copy output back to arr
    for i in range(n):
        arr[i] = output[i]


# Input format: space-separated integers
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
n = len(arr)
k = max(arr) + 1  # max element + 1 is the range

countSort(arr, n, k)

print("Sorted array:")
print(*arr)
