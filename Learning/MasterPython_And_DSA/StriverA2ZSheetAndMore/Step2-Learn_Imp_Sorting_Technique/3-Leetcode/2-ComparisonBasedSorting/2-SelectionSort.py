
'''
It also is not a stable sorting algorithm. For example consider the collection [4, 2, 3, 4, 1]. After the first round of selection sort, we get the array [1, 2, 3, 4, 4]. This array is sorted, but it does not preserve the ordering of equal elements.
'''
from typing import List

class Solution:
    def selection_sort(self, lst: List[int]) -> None:
        """
        Mutates lst so that it is sorted via selecting the minimum element and
        swapping it with the corresponding index.
        """
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                # Update minimum index
                if lst[j] < lst[min_index]:
                    min_index = j
            # Swap current index with minimum element in rest of list
            lst[i], lst[min_index] = lst[min_index], lst[i]

# Input
user_input = input("Enter a list of integers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Sort using selection sort
sol = Solution()
sol.selection_sort(numbers)

# Output
print("Sorted list:", numbers)
