'''
Problem :- https://leetcode.com/problems/spiral-matrix/description/

Probnlem:- Spiral Matrix
'''


# Solution 1 Optimal 
'''
Time Complexity: O(m x n) { Since all the elements are being traversed once and there are total n x m elements ( m elements in each row and total n rows) so the time complexity will be O(n x m)}.

Space Complexity: O(n) { Extra Space used for storing traversal in the ans array }.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix),len(matrix[0])
        right, left, top, bottom = m-1, 0, 0, n-1
        ans = []
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if top<=bottom:
                for i in range(right, left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            if left<=right:
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
        return  ans