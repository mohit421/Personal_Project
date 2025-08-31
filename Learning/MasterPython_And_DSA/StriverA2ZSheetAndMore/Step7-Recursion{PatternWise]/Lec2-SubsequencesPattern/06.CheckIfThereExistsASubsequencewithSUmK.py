'''
Check if there exists a subsequence with sum K

'''


#User function Template for python3

class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        
        def helper(i, s):
            # base case: if we've considered all elements
            if i == N:
                return s == K
            
            # if sum exceeds K, no need to continue
            if s > K:
                return False
            
            # include arr[i]
            if helper(i + 1, s + arr[i]):
                return True
            
            # exclude arr[i]
            if helper(i + 1, s):
                return True
            
            return False
        
        return helper(0, 0)
        