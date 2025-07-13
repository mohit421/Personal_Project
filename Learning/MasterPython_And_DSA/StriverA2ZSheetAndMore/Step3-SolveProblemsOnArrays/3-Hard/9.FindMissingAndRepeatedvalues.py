'''
link:- https://leetcode.com/problems/find-missing-and-repeated-values/description/
'''

# Solution 1 
'''
TC:- O(N^2) + O(N^2) = O(2*N^2) = O(N^2)
SC:- O(N^2) :- bcuz storing freq element till 1 to n^2

'''
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        a,b = 0,0
        n = len(grid)
        mpp = {}
        for arr in grid:
            for j in arr:
                mpp[j] = mpp.get(j,0) + 1

        repeated = missing = 0
        total = n*n
        for i in range(1,total+1):
            count = mpp.get(i,0)
            if count == 0:
                missing = i
            elif count == 2:
                repeated = i
        return [repeated,missing]
    
# Similar to above but using defaultdict()

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = defaultdict(int)
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        missing, repeated = 0,0

        for i in range(1,n*n+1):
            if count[i] == 0:
                missing = i
            elif count[i] == 2:
                repeated = i
        return [repeated,missing]
    

# Similar to aboe but uisng simple {}

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in count:
                    count[grid[i][j]] = 0
                count[grid[i][j]] += 1

        missing, repeated = 0,0

        for i in range(1,n*n+1):
            if i not in count:
                missing = i
            elif count[i] == 2:
                repeated = i
        return [repeated,missing]

# Solution 2  using mathematical equations
'''
TC:- O(n^2)
SC:- O(1)
'''

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = n*n
        expected_sum = total * (total + 1) // 2
        expected_sq_sum = total * (total + 1) * (2 * total + 1) // 6

        actual_sm = actual_sq_sum = 0

        for row in grid:
            for col in row:
                actual_sm += col
                actual_sq_sum += col*col
        
        diff = actual_sm - expected_sum #y-x
        sq_diff = actual_sq_sum - expected_sq_sum   #y^2 - x^2
        # y^2-x^2 = (y+x)(y-x)
        sum_yx = sq_diff//diff  # y+x
        y = (diff+sum_yx)//2
        x = y- diff
        return [y,x]

