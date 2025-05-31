'''
Link:- https://leetcode.com/explore/learn/card/sorting/695/non-comparison-based-sorts/4437/
'''

'''
Time Complexity:

| Step                              | Time       | Explanation                         |
| --------------------------------- | ---------- | ----------------------------------- |
| `max(lst)`                        | `O(n)`     | Scans the list once to find the max |
| Initialize `counts`               | `O(K + 1)` | List of zeros from `0` to `K`       |
| Count frequencies (`for elem...`) | `O(n)`     | Goes through each element once      |
| Compute starting indices          | `O(K + 1)` | Loops through the `counts` array    |
| Build `sorted_lst`                | `O(n)`     | Places each element once            |
| Copy back to original list        | `O(n)`     | Final overwrite                     |


Space Complexity:-

| Structure    | Space      | Explanation                     |
| ------------ | ---------- | ------------------------------- |
| `counts`     | `O(K + 1)` | For counting and index tracking |
| `sorted_lst` | `O(n)`     | Holds sorted values temporarily |


Time and space complexity:- O(n + K)
'''

# Code 


class Solution:
    def counting_sort(self, lst) -> None:
        """
        Sorts a list of integers where minimum value is 0 and maximum value is K
        """
        K = max(lst)
        counts = [0] * (K + 1)
        for elem in lst:
            counts[elem] += 1

        # we now overwrite our original counts with the starting index
        # of each element in the final sorted array
        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(lst)

        for elem in lst:
            sorted_lst[counts[elem]] = elem
            counts[elem] += 1

        for i in range(len(lst)):
            lst[i] = sorted_lst[i]

# ---- USER INPUT PART ----
if __name__ == "__main__":
    input_str = input("Enter a list of non-negative integers (comma-separated): ")
    
    # Convert string input to list of integers
    try:
        input_list = list(map(int, input_str.split(',')))
        if any(n < 0 for n in input_list):
            raise ValueError("Counting sort only works with non-negative integers.")

        s = Solution()
        s.counting_sort(input_list)
        print("Sorted list:", input_list)
    
    except ValueError as e:
        print("Invalid input:", e)


'''

Above code 
-Assumes all elements are non-negative.

Works only when min(lst) >= 0.

If list has -1, -5, etc., it'll crash with IndexError.


Why use the new Shifted code

| Feature                   | Non-Shifted Code              | Shifted Code (Current) |
| ------------------------- | ----------------------------- | ---------------------- |
| Supports negative numbers | ❌ No                          | ✅ Yes                  |
| Flexible for any int list | ❌ No                          | ✅ Yes                  |
| Risk of crash             | ❌ `IndexError` if element < 0 | ✅ None                 |
| General-purpose usage     | ❌ Limited                     | ✅ Broad  



Handles negative numbers by shifting all values into a non-negative range.

Ensures counting sort works on any list of integers, positive or negative.              |




We use the shifted version because it makes Counting Sort:

Safe for all inputs (negative, positive, zero)

More general-purpose

Still keeps O(n + K) time and space complexity
'''
# We use shifted version of code

# Code

class Solution:
    def counting_sort(self,lst)->None:
        '''
        Sorts a list of integers where minimum value is 0 maximum value is k

        '''
        shifts = min(lst)
        k = max(lst)- shifts
        counts = [0]*(k+1)
        for elem in lst:
            counts[elem-shifts] += 1

        starting_index = 0
        for i,count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0]*len(lst)
        for elem in lst:
            sorted_lst[counts[elem-shifts]] = elem 
            counts[elem-shifts] += 1

        for i in range(len(lst)):
            lst[i] = sorted_lst[i]
        return lst


# ✅ User input
if __name__ == "__main__":
    input_str = input("Enter a list of integers separated by spaces: ")
    user_list = list(map(int, input_str.strip().split()))

    solution = Solution()
    sorted_list = solution.counting_sort(user_list)
    print("Sorted list:", sorted_list)