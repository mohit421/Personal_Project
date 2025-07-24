'''

'''

# Brute force appraioch

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        return False

# Better solution 

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
            if self.binarySearch(matrix[i], target):
                return True
        return False
    

#  Better solution 2
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
We can't do like preious optimised solution bcuz in this row and column both sorted and in previous question only row in sorted i.e., row major matrix 
'''

'''
Time Complexity: O(N+M), where N = given row number, M = given column number.
Reason: We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). So, the total distance can be at most (N+M). So, the time complexity is O(N+M).

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        row, col = 0, m-1
        while row<n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False
