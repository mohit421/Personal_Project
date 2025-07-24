
'''
Complexity Analysis

Time Complexity: O(N X M), where N = given row number, M = given column number.
Reason: In order to traverse the matrix, we are using nested loops running for n and m times respectively.

Space Complexity: O(1) as we are not using any extra space.
'''


# Using brute force

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        return False
    
# USing binary Search  better solution 
'''
Complexity Analysis

Time Complexity: O(N + logM), where N = given row number, M = given column number.
Reason: We are traversing all rows and it takes O(N) time complexity. But for all rows, we are not applying binary search rather we are only applying it once for a particular row. That is why the time complexity is O(N + logM) instead of O(N*logM).

Space Complexity: O(1) as we are not using any extra space.
'''

class Solution:
    def binarySearch(self, nums:List[int], target: int)-> bool:
        lo,hi = 0, len(nums) - 1
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return True
            elif  target<nums[mid]:
                hi = mid -1
            else:
                lo = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            if self.binarySearch(matrix[i],target):
                return True
        return False
    
#  More better solution 
'''

'''
class Solution:
    def binarySearch(self, nums:List[int], target: int)-> bool:
        lo,hi = 0, len(nums) - 1
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return True
            elif  target<nums[mid]:
                hi = mid -1
            else:
                lo = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            if matrix[i][0] <= target and target <= matrix[i][m-1]:
                if self.binarySearch(matrix[i], target):
                    return True
        return False



# Optimised solution 
'''
We have to think hypothecally 2D array as 1D array
- Convert the 1D to 2D
row: index/(no of elem in column-> row = index/m
col : index%(no of element in column) ->col = index%m
for eg: col = m=4, index = 5
row = 5/4  = 1
col = 5%4 = 1
so we have mat[row][col] in 1D array


Complexity Analysis

Time Complexity: O(log(NxM)), where N = given row number, M = given column number.
Reason: We are applying binary search on the imaginary 1D array of size NxM.

Space Complexity: O(1) as we are not using any extra space.
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        lo,hi = 0, n*m-1
        while lo<=hi:
            mid = (lo+hi)//2
            row,col = mid//m, mid%m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
