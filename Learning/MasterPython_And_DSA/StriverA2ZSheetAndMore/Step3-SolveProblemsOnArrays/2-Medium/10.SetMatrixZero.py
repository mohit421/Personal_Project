'''
Complexity Analysis

Time Complexity: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: Firstly, we are traversing the matrix to find the cells with the value 0. It takes O(N*M). Now, whenever we find any such cell we mark that row and column with -1. This process takes O(N+M). So, combining this the whole process, finding and marking, takes O((N*M)*(N + M)).
Another O(N*M) is taken to mark all the cells with -1 as 0 finally.

Space Complexity: O(1) as we are not using any extra space.

'''

# Brute force Solution 1 
#  DOn't take care of negatice -1 in the matrix

class Solution:

    def markRow(self,matrix, n,m, i):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1
    def markCol(self, matrix, n,m,j):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    self.markRow(matrix,n,m,i)
                    self.markCol(matrix,n,m,j)
        
        for i  in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0





# SOlution 2 Better solution take care of negative numbers
'''
Complexity Analysis

Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

Space Complexity: O(N) + O(M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: O(N) is for using the row array and O(M) is for using the col array.
'''
class Solution:

    def markRow(self,matrix, n,m, i):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1
    def markCol(self, matrix, n,m,j):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        col = [0]*m
        row = [0]*n
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i] = 1
                    col[j] = 1
        
        for i  in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0


# Solution 3 Optimal soluton 

'''
Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: In this approach, we are also traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

Space Complexity: O(1) as we are not using any extra space.
'''

class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix) , len(matrix[0])
        col0 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] != 0:
                    # check for row and col
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
        
