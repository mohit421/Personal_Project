

class Solution:
    def bubble_sort(self, lst: list[int])-> None:

        has_swapped = True 
        while has_swapped:
            has_swapped = False 
            for i in range(len(lst)-1):
                if lst[i] > lst[i+1]:
                    lst[i],lst[i+1] = lst[i+1],lst[i] 
                    has_swapped = True

user_input = input("Enter a list of integers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Sort using selection sort
sol = Solution()
sol.bubble_sort(numbers)

# Output
print("Sorted list:", numbers)