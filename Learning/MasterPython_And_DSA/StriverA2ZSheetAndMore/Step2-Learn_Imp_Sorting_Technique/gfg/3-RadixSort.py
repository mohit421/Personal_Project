'''

- Like counting sort,it also a linear time algorithm if our data is within a limited range
- We already have counting sort why we need another sorting algorithm
- Counting sort will take time O(n+k), where k is range of element
- If k is n^2 then counting sort will take O(n^2)
- which is worse than standard comparison based algorithm like Merge and Heap sort
- Radix sort is a sorting algorithm that support linear time even for a larger range .
- It works for linear , works in linear time 0 to n^2 or 0 to n^3
- It uses counting sort as a subroutine to sort the element
- Like counting sort it's also not a comparison based algorithm beccause if we have normal comparison based algorithm, then we can't sort the elements in time complexity less than O(NlogN)
- It sort the element in linear time if it is in small range


                            Idea

- [319,212,6,8,100,50] 
- Rewriting number with leading zeros :[319,212,006,008,319]
- Stable sort according to the last digit (least significant digit) : [100,050,212,006,008,319]
- Stable sort according to the middle digit: [100,006, 050, 008, 212, 319]
- Stable sort acc. to most significant digit: [006,008,050,100,212,319]


                    Time Complexity

                    Final Radix Sort Time Complexity:
O(n × log₁₀(mx))

Or generally:

O(n × d) where d is number of digits

                        Comparison

| Sort       | Time Complexity  | Stable? | When to Use                                        |
| ---------- | ---------------- | ------- | -------------------------------------------------- |
| Count Sort | O(n + k)         | Yes     | When `k` is small and all numbers are non-negative |
| Radix Sort | O(n × log₁₀(mx)) | Yes     | When integers are large but digit count is small   |

'''

#                            Code

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

def radixSort(arr,n):
    # Find the maximum number to know the number of digits
    mx = max(arr)
    exp = 1
    while mx // exp > 0:
        countingSort(arr, n, exp)
        exp *= 10

def countingSort(arr,n,exp):
    count = [0]*10 
    output = [0]*n 
    for i in range(n):
        index = (arr[i]//exp)%10
        count[index] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    for i in range(n-1,-1,-1):
        index = (arr[i]//exp)%10
        output[count[index]-1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

if __name__ == "__main__":
    arr = list(map(int, input("Enter integers separated by space: ").split()))
    n = len(arr)

    # Choose which sort to use:
    print("Choose sorting method:\n1. Count Sort (only non-negative integers < k)\n2. Radix Sort")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        k = max(arr) + 1
        countSort(arr, n, k)
    elif choice == 2:
        radixSort(arr, n)
    else:
        print("Invalid choice. Exiting.")
        exit()

    print("Sorted array:", arr)