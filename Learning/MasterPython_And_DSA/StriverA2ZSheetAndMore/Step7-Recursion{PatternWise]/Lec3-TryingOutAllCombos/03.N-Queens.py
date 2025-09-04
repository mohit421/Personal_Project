'''
N-Queens | Leetcode Hard | Backtracking
'''

# Solution 1
'''
- Every Rows must have only 1 Queens
- Every Columns must have only 1 Queens
- None of the queens attack each other
- Queens can attack in 8 Directions


'''

# Brute force

'''
Time Complexity: Exponential in nature since we are trying out all ways, to be precise its O(N! * N).

Space Complexity: O( N2 )
'''

class Solution:

    def checkPossible(self, row, col, lstStr, n):
        dbRow = row
        dbCol = col

        while row>= 0 and col >= 0:
            if lstStr[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        
        row= dbRow
        col = dbCol

        while col>=0:
            if lstStr[row][col] == 'Q':
                return False
            col -= 1



        row= dbRow
        col = dbCol

        while row<n and col>=0:
            if lstStr[row][col] == 'Q':
                return False
            row += 1
            col -= 1

        return True


    def solve(self, col, lstStr, ans, n):
        if col == n:
            ans.append(list(lstStr))
            return
        
        for row in range(n):
            if self.checkPossible(row, col, lstStr, n):
                lstStr[row] = lstStr[row][:col] +  "Q" + lstStr[row][col+1:]
                self.solve(col+1,lstStr, ans , n)
                lstStr[row] = lstStr[row][:col] +  "." + lstStr[row][col+1:]
            


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        lstStr = ['.'*n for _ in range(n)]

        self.solve(0, lstStr, ans,n)
        return ans



# Solution 
# Optimal
'''
Time Complexity: Exponential in nature since we are trying out all ways, to be precise it is O(N! * N).

Space Complexity: O(N)
'''

class Solution:

    def solve(self, col, ans, lst, n, leftRow, lowerDiagonal, upperDiagonal):

        if col == n:
            ans.append(lst[:])
            return
        
        for row in range(n):
            if leftRow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n-1+col-row] == 0:
                lst[row] = lst[row][:col] + "Q" + lst[row][col+1:]
                leftRow[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n-1+col-row] = 1
                self.solve(col+1, ans, lst, n, leftRow, lowerDiagonal, upperDiagonal)

                lst[row] = lst[row][:col] + "." + lst[row][col+1:]
                leftRow[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n-1+col-row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        lst = ['.'*n for _ in range(n)]
        leftRow = [0]*n
        lowerDiagonal = [0]*(2*n-1)
        upperDiagonal = [0]*(2*n-1)
        self.solve(0, ans, lst, n, leftRow, lowerDiagonal, upperDiagonal)
        return ans
