

from typing import List

class Solution:
    def sort_by_length(self, lst: List[str]) -> None:
        """
        Sorts a list of strings by the length of each string (in-place)
        """        
        lst.sort(key=lambda x: len(x))  # or simply: lst.sort(key=len)

# Input
user_input = input("Enter a list of words separated by spaces: ")
words = user_input.split()

# Sort
sol = Solution()
sol.sort_by_length(words)

# Output
print("Sorted by length:", words)
