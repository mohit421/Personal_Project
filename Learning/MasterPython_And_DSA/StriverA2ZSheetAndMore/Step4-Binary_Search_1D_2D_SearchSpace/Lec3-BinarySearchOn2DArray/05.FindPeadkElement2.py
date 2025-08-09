'''

'''


# Optimised approach



class Solution:
    def findPeakIndexEle(self, mat: List[List[int]], n: int, m: int, col: int) -> int:
        maxVal, idx = -1, -1
        for i in range(n):
            if mat[i][col] > maxVal:
                maxVal = mat[i][col]
                idx = i
        return idx
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n,m = len(mat), len(mat[0])
        lo,hi = 0,m-1
        while lo <= hi:
            mid = (lo+hi)//2
            maxRowIdx = self.findPeakIndexEle(mat,n,m,mid)
            left = mat[maxRowIdx][mid - 1] if mid - 1 >= 0 else -1
            right = mat[maxRowIdx][mid + 1] if mid + 1 < m else -1
            if mat[maxRowIdx][mid] > left and mat[maxRowIdx][mid]> right:
                return [maxRowIdx,mid]
            elif mat[maxRowIdx][mid] < left:
                hi = mid - 1
            else:
                lo = mid + 1

                
        return [-1,-1]