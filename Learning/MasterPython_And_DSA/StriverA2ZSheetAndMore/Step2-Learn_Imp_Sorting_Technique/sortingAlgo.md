# Selection Sort

    - theta(N^2)
    - Does less memroy writes compared to Quick SOrt, Merge Sort, Insertion SOrt, etc, but cycle sort is optimal in terms of memory writes
    - Basic Idea for Heap Sort
    - Not stable
    - In-place

# Bubble Sort

    - For N element, it takes N-1 passes
    - Bubble sort is stable and it also inplace
    Inplace(It doesn't require extra array to copy the original elements, It modifies the lement within the array  only)
    - O(N^2)

# Insertion Sort

    - O(N^2) worst case
    - In-place and stable
    - used in practice for small arrays(Tim sort and intro sort)
    - O(N) for best case
    - to maintain stability of algorithm, we don't put equal to sign
    - If we put then algorithm wouldn't be stable but still it work

# Merge Sort

    - Divide and Conquer Algorithm (divide, conquer and merge)
    - Stable Algorithm
    - Theta(nlogn) time and O(n) Auxiliary space for arrays
    - Well suited for linked lists works in O(1) auxiliary space
    - Used in external sorting
    - In general for arrays, QuickSort Outperforms

    - Java 8 uses both Quick Sort & Merge Sort depending upon the input type
