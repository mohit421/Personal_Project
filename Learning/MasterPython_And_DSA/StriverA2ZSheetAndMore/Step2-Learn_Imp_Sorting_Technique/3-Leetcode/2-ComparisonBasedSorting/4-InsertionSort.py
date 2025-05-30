'''
Insertion Sort
'''

class Solution:
    def insertion_sort(self, lst: list[int]) -> None:
        for i in range(1, len(lst)):
            current_idx = i
            while current_idx > 0 and lst[current_idx - 1] > lst[current_idx]:
                lst[current_idx], lst[current_idx - 1] = lst[current_idx - 1], lst[current_idx]
                current_idx -= 1


# Accept user input
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, user_input.strip().split()))
    
    sol = Solution()
    sol.insertion_sort(num_list)
    
    print("Sorted list:", num_list)


