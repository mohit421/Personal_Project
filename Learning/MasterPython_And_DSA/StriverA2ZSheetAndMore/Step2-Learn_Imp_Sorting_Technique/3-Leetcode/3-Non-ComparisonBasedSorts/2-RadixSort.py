'''
Link:- https://leetcode.com/explore/learn/card/sorting/695/non-comparison-based-sorts/4438/
'''

from typing import List

class Solution:
    def counting_sort(self, lst: List[int], place_val: int, K: int = 10) -> None:
        """
        Sorts a list of integers based on digit at place_val using counting sort.
        """
        counts = [0] * K

        for elem in lst:
            digit = (elem // place_val) % 10
            counts[digit] += 1

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)
        for elem in lst:
            digit = (elem // place_val) % 10
            sorted_lst[counts[digit]] = elem
            counts[digit] += 1

        for i in range(len(lst)):
            lst[i] = sorted_lst[i]

    def radix_sort(self, lst: List[int]) -> None:
        if not lst:
            return

        shift = min(lst)
        lst[:] = [num - shift for num in lst]
        max_elem = max(lst)

        place_val = 1
        while place_val <= max_elem:
            self.counting_sort(lst, place_val)
            place_val *= 10

        lst[:] = [num + shift for num in lst]

# -----------------------------
# Take user input and apply sort
# -----------------------------

if __name__ == "__main__":
    user_input = input("Enter integers separated by spaces: ")
    arr = list(map(int, user_input.strip().split()))

    solver = Solution()
    solver.radix_sort(arr)

    print("Sorted list:", arr)
