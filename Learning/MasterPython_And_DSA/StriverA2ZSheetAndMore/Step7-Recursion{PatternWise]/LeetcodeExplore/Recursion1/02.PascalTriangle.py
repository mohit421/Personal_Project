'''

'''

# Recursive Solution 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        prev = self.generate(numRows-1)
        lastRow = prev[-1]
        
        newRow = [1]
        for i in range(len(lastRow)-1):
            newRow.append(lastRow[i]+lastRow[i+1])
        newRow.append(1)
        return prev + [newRow]



# Solution 2

class Solution:
    def pascal(self, n: int, v: List[List[int]]) -> None:
        # Base case
        if n == 1:
            v.append([1])
            return

        # Build triangle up to n-1 first
        self.pascal(n - 1, v)
        prev = v[-1]     # last row so far
        row = [1]        # start with 1
        for i in range(1, len(prev)):
            row.append(prev[i-1] + prev[i])
        row.append(1)    # end with 1
        v.append(row)

    def generate(self, numRows: int) -> List[List[int]]:
        v: List[List[int]] = []
        self.pascal(numRows, v)
        return v