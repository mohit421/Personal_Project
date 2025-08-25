'''
Problem link:- https://leetcode.com/problems/pascals-triangle/
'''




# Three variation of a Problems are :-

'''
       1
    1    1
   1   2   1
  1  3   3   1    
 1  4   6   4  1
1  5  10  10  5  1

1. Given row and col, and ask for the element at that place where,
rowNum = 5 and   colNUm = 3
so, ans is 6 at [r][c] = [5][3] = 6


2. Print any nth row of pascal tirangle
where, N = 5

1 4 6 4 1

3. Given N, Print the entire triangle
where, N = 6

'''

# Variation 1
'''
nCr = n!/(n! * (n-r)!)
r = 5, c = 3
rCc = r!/(c! * (r-c)!) = 4C2 = (4*3*2*1)/((2*1)(2*1)) = 6

- How to simplify above one 

7C2 = 7*6*(5*4*3*2*1)/2*1 *(5*4*3*2*1) = 7*6/(2*1) 

from 7 goto two places like r = 2 that's sthe trick

One more Examples:-

10C3 = 10*9*8/3*2*1 = 10/1 * 9/2 * 8/3

'''
# Solution variation 1


'''
Complexity Analysis
Time Complexity: O(c), where c = given column number.
Reason: We are running a loop for r times, where r is c-1.

Space Complexity: O(1) as we are not using any extra space.
'''

import math

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element

if __name__ == '__main__':
    r = 5 # row number
    c = 3 # col number
    element = pascalTriangle(r, c)
    print(f"The element at position (r,c) is: {element}")
    
        
        

# Variation 2

'''
Given the row number n. Print the n-th row of Pascal’s triangle.

Our first observation regarding Pascal’s triangle should be that the n-th row of the triangle has exactly n elements. With this observation, we will proceed to solve this problem.
'''
'''
Complexity Analysis
Time Complexity: O(n*r), where n is the given row number, and r is the column index which can vary from 0 to n-1.
Reason: We are calculating the element for each column. Now, there are total n columns, and for each column, the calculation of the element takes O(r) time where r is the column index.

Space Complexity: O(1) as we are not using any extra space.
'''

import math

def nCr(n, r):
    res = 1
    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(n):
    # printing the entire row n:
    for c in range(1, n+1):
        print(nCr(n-1, c-1), end=" ")
    print()

if __name__ == "__main__":
    n = 5
    pascalTriangle(n)
    

# Variation 3
'''
Print the triangle with given n



Complexity Analysis
Time Complexity: O(n2), where n = number of rows(given).
Reason: We are generating a row for each single row. The number of rows is n. And generating an entire row takes O(n) time complexity.

Space Complexity: In this case, we are only using space to store the answer. That is why space complexity can still be considered as O(1).
'''

class Solution:
    def generateRow(self,r):
        res = 1
        ansRow = [1]
        for i in range(1,r):
            res *= (r-i)
            res //=i
            ansRow.append(res)
        return ansRow
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows+1):
            ans.append(self.generateRow(i))
        return ans
            



# 2nd SOlution 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mat = []
        for i in range(numRows):
            vec = [1]*(i+1)
            for j in range(1,i):
                vec[j] = mat[i-1][j-1] + mat[i-1][j]
            mat.append(vec)
        return mat


'''

'''

# SOlution 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res