'''
'''



# Partially recursive code 

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = self.getRow(rowIndex-1)
        row = [1]
        for i in range(1,len(prev)):
            row.append(prev[i-1]+ prev[i])
        row.append(1)
        return row
    



# Fully recursive code
'''
Time Complexity

Outer recursion (getRow)

To compute row n, you first compute row n-1, then row n-2, ..., all the way down to row 0.

So rows 0, 1, 2, …, n are built.

Work per row

Building row k requires:

computing row k-1 (recursive call), and

computing the interior values of length k-1 using buildRow.

That’s O(k) work for row k.

Total work

Sum over all rows from 0..n:

✅ Time complexity: O(n²)

🔹 Space Complexity

Output space

Final row has n+1 numbers → requires O(n) space.

Recursion depth (outer getRow)

The recursion depth = n (you call getRow(n-1), getRow(n-2), …, getRow(0)).

So stack depth is O(n).

Recursion depth (inner buildRow)

When building row k, buildRow runs recursion up to length of prev, i.e., O(k).

For the largest row (row n), this depth is O(n).

But this recursion happens after prev is already computed, so it does not stack with the outer recursion all the way — still bounded by O(n).

Total auxiliary space

Maximum call stack depth: O(n).

Output row: O(n).

Combined: O(n).

✅ Space complexity: O(n)

🔹 Summary

Time complexity: O(n²)

Space complexity: O(n)
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        # Get the previous row recursively
        prev = self.getRow(rowIndex - 1)
        
        # Recursive helper to build the middle of the row
        def buildRow(i: int) -> List[int]:
            if i == len(prev):     # finished scanning prev
                return []
            return [prev[i-1] + prev[i]] + buildRow(i + 1)
        
        # Combine: leading 1, middle part, trailing 1
        return [1] + buildRow(1) + [1]


