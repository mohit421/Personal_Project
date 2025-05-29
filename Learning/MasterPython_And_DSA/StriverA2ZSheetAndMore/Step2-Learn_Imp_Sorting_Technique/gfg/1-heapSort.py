'''
- Basic Idea of Heap SOrt is based on Selection SOrt algorithm
- Heap Sort does an optimization over selection sort, uses the same idea but for finding the maximum element instead of doing linear search.
- Heap SOrt uses max Heap data structure

Q) What we do in Heap Sort?
Ans:- We have given an array
- We restructure the array or rearrange the elements of this array so that they form a max-heap and building a max_heap or min-heap from a random array in O(N) time
- SO we got our Max heap as our 1st step
- After building the maxHeap we swap the last element with the root of the Max Heap.
- SO our maximum element fo to the end like we do in selection sort
- After that we simply do , heapify bcuz heapify is an operation that works well when the sub trees are heapified only root is disturbed
- So we fix the root heapify operation and we keep on repeating this process
- Every array can be seen as a complete Binary tree


                    Step 1: Build a Max heap

- If we won't sort an array in increasing or we use max heap otherwise use minHeap for decreasing order
- Our traget is to convert the binary three into max heap
- To convert binary tree into max heap , we call a process called BuildHeap
- What is BuildHeap process does?
- It begin from the last internal node, goes till root of the tree, which is zero index and keeps calling heapify for every node it visits.

Q - How maxHeapify work?
- It find the largest of three things node and its two child and swap the largest with the node if one of its child is largest.


- Complexity Analysis of Heap Sort
Time Complexity: O(n log n)
Auxiliary Space: O(log n), due to the recursive call stack. However, auxiliary space can be O(1) for iterative implementation.

- Important points about Heap Sort
Heap sort is an in-place algorithm.
Its typical implementation is not stable but can be made stable (See this)
Typically 2-3 times slower than well-implemented QuickSort. The reason for slowness is a lack of locality of reference.
'''

def heapify(arr, n, i):
    largest = i  # initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root node
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr, n):
    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()


# 🔸 Accepting user input
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
heapSort(arr, len(arr))
print("Sorted array is:")
printArray(arr)
