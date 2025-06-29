'''
Problem:-48. Rotate Image

Link:- https://leetcode.com/problems/rotate-image/
'''


# Solution 1 Brute force

'''
Complexity Analysis

Time Complexity: O(N*M)+ O(N*M) to linearly iterate and put it into some other matrix.

Space Complexity: O(N*N) to copy it into some other matrix.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])
        rotated = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                rotated[j][n-i-1] = (matrix[i][j])
        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = rotated[i][j]
                
        


# Solution 2 Optimal one
'''

Complexity Analysis

Time Complexity: O(N*N) + O(N*N).One O(N*N) is for transposing the matrix and the other is for reversing the matrix.

Space Complexity: O(1).
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

        
                
    

# optimise like above

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])
        for i in range(n-1):
            for j in range(i+1,m):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

        
                
        