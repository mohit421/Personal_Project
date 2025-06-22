'''
Problem Link:- https://leetcode.com/problems/subarray-sum-equals-k/
'''

# Solution 1 :- Brute Force 


'''
Complexity Analysis

Time Complexity: O(N3) approx., where N = size of the array.
Reason: We are using three nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.


61/93 test cases passed
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i,n):
                s = 0
                for m in  range(i,j+1):
                    s += nums[m]
                
                if s == k:
                    count += 1
        return count
    

# Solution 2 Optimizing the Naive Approach (Using two loops): 

'''
Complexity Analysis

Time Complexity: O(N^2) approx., where N = size of the array.
Reason: We are using two nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.




'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                if s == k:
                    count += 1
        return count
    


# Solution 3 Using Hashing  better solution 

'''
| Metric               | Value                    |
| -------------------- | ------------------------ |
| **Time Complexity**  | `O(n)`                   |
| **Space Complexity** | `O(n)`                   |
| **Approach**         | Optimal for this problem |


'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        sum_val = 0
        prefixSum = {0:1}

        for num in nums:
            sum_val += num

            # Check if we've seen (sum-k)  before
            if sum_val -k in prefixSum:
                count += prefixSum[sum_val-k]
            
            # Add current sum to our map

            prefixSum[sum_val] = prefixSum.get(sum_val,0) + 1

        return count
        

'''
Using defaultdict improved above code

| Metric | Value                 |
| ------ | --------------------- |
| Time   | O(n)                  |
| Space  | O(n) (for prefix map) |

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSumMap = defaultdict(int)
        preSumMap[0] = 1  # Important: to handle subarrays starting at index 0

        currentSum = 0
        count = 0

        for num in nums:
            currentSum += num
            rem = currentSum - k

            # If rem exists, we can form a subarray ending here with sum == k
            count += preSumMap[rem]

            # Update prefix sum count
            preSumMap[currentSum] += 1

        return count
    

#  Optimized solutionS

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = {0:1}

        for n in nums:
            curSum += n
            diff = curSum -k

            res += prefixSum.get(diff,0)

            prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
        return res 
        
'''
We can not use Sliding window bcuz it only works for non-negative number 
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        right, left = 0,0
        count = 0
        currSum = 0
        n = len(nums)
        while right<n:
            currSum += nums[right]
            right += 1
            while left <= right and currSum > k:
                currSum -= nums[left]
                left += 1
            
            if currSum == k:
                count += 1

        return count

