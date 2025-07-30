'''

'''


# Brute force

#User function Template for python3
'''
Complexity Analysis

Time Complexity: O(MXN) + O(MXN(log(MXN))), where M = number of row in the given matrix, N = number of columns in the given matrix

Reason: At first, we are traversing the matrix to copy the elements. This takes O(MXN) time complexity. Then we are sorting the linear array of size (MXN), that takes O(MXN(log(MXN))) time complexity

Space Complexity: O(MXN) as we are using a temporary list to store the elements of the matrix.
'''
class Solution:
    def median(self, mat):
    	#code here 
    	ans = []
    	n,m = len(mat), len(mat[0])
    	for i in range(n):
    	    for j in range(m):
    	        ans.append(mat[i][j])
        ans.sort()
        return ans[(m * n) // 2]
	

# Optimised solution
#User function Template for python3

class Solution:
    def upperbound(self, arr, x, m):
        lo,hi,ans = 0, m-1, m
        while lo<=hi:
            mid = (lo+hi)//2
            if arr[mid]>x:
                ans = mid
                hi = mid -1
            else:
                lo = mid + 1
        return ans
    
    def countSmallEq(self, mat,n,m, mid):
        cnt = 0
        for i in range(n):
            cnt += self.upperbound(mat[i],mid, m )
        return cnt
    def median(self, mat):
    	#code here 
    	n,m = len(matrix), len(matrix[0])
        lo, hi = float('inf'), float('-inf')
        for i in range(n):
            lo = min(lo, mat[i][0])
            hi = max(hi,mat[i][m-1])
        
        req = m*n//2
        while lo<= hi:
            mid = (lo+hi)//2
            smallEquals = self.countSmallEq(mat,n,m,mid)
            if smallEquals <= req:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo
        