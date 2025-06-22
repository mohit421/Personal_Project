'''
Problem Link:- https://leetcode.com/problems/missing-number/
'''

# Solution 1  Brute force approach



def missing_number(a, N):
    # Outer loop that runs from 1 to N:
    for i in range(1, N + 1):
        # flag variable to check if an element exists
        flag = 0

        # Search the element using linear search:
        for j in range(len(a)):
            if a[j] == i:
                # i is present in the array:
                flag = 1
                break

        # check if the element is missing (i.e., flag == 0):
        if flag == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missing_number(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()




# Solution 2 better solution using hashing 
'''
Time Complexity: O(N) + O(N) ~ O(2*N),  where N = size of the array+1.
Reason: For storing the frequencies in the hash array, the program takes O(N) time complexity and for checking the frequencies in the second step again O(N) is required. So, the total time complexity is O(N) + O(N).

Space Complexity: O(N), where N = size of the array+1. Here we are using an extra hash array of size N+1.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums) +1
        hash = [0]*(N+1)
        for i in range(N-1):
            hash[nums[i]] += 1
        
        for i in range(0,N+1):
            if hash[i] == 0:
                return i
        return -1




# Solution 3
'''

'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
    


# Solution 4

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = len(nums)
        for i in range(n):
            res += i- nums[i]
        return res
    

# Solution 5

'''
Time Complexity: O(N), where N = size of array+1.
Reason: Here, we need only 1 loop to get the sum of the array elements. The loop runs for approx. N times. So, the time complexity is O(N).

Space Complexity: O(1) as we are not using any extra space
'''

def missingNumber(a, N):
    # Summation of first N numbers:
    summation = (N * (N + 1)) // 2

    # Summation of all array elements:
    s2 = sum(a)

    missingNum = summation - s2
    return missingNum


# solution 6 using XOR 
'''
Time Complexity: O(N), where N = size of array+1.
Reason: Here, we need only 1 loop to calculate the XOR. The loop runs for approx. N times. So, the time complexity is O(N).

Space Complexity: O(1) as we are not using any extra space.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1, xor2 = 0,0 
        for i in range(len(nums)):
            xor1 = xor1^nums[i]
            xor2 = xor2^(i)
        xor2 = xor2^(len(nums))
        return xor1^xor2
