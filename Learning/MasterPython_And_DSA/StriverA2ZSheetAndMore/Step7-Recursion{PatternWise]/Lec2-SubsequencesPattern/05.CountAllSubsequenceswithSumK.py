'''

'''


# USing recurison got TLE



class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        cnt = 0

        def helper(i,mini, maxi):
            nonlocal cnt

            if i == len(nums):
                if mini + maxi <= target:
                    cnt += 1
                return
            
            # Case 1 include nums[i] in the subsequence

            new_min = min(mini, nums[i])
            new_maxi = max(maxi, nums[i]) 

            helper(i+1, mini, maxi)
            # Case 2: Exclude nums[i] from the subsequence
            helper(i+1, new_min, new_maxi)
        
        helper(0, float("inf"), float("-inf"))
        return cnt % MOD  # Return the result modulo 10^9 + 7
    


# Solution 
# /Using Recursion and two pointer 


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sorting the array to make min and max easy to track
        MOD = 10**9 + 7
        cnt = 0
        
        # Helper function to count valid subsequences recursively
        def helper(left, right):
            nonlocal cnt
            
            # Base case: if left pointer exceeds right pointer, no valid subsequence
            if left > right:
                return
            
            # If nums[left] + nums[right] <= target, we can count all subsequences between left and right
            if nums[left] + nums[right] <= target:
                # 2^(right - left) subsequences can be formed between left and right
                cnt += pow(2, right - left, MOD)
                cnt %= MOD
                # Move left pointer to the right
                helper(left + 1, right)
            else:
                # If nums[left] + nums[right] > target, move the right pointer to the left
                helper(left, right - 1)

        helper(0, len(nums) - 1)  # Start recursion with left pointer at 0 and right pointer at the last index
        return cnt % MOD  # Return the result modulo 10^9 + 7
