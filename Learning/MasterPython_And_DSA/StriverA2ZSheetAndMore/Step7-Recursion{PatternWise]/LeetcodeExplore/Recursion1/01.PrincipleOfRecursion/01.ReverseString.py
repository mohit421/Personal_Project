'''

'''

# Iterative Solution 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Recursive Soluition 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        revStr = []
        
        def build_reverse(i:int):
            if i == len(s):
                return
            build_reverse(i+1)
            revStr.append(s[i])
        build_reverse(0)
        
        def copy_back(i:int):
            if i == len(s):
                return
            s[i] = revStr[i]
            copy_back(i+1)
        copy_back(0)
    




# Iterative Sioution 2

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        revStr = []
        for i in range(len(s)):
            revStr.append(s[len(s)-i-1])
        
        # Copy contents back into s
        for i in range(len(s)):
            s[i] = revStr[i]







# Recursive Soluiion 2

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left: int, right: int):
            if left>=right:
                return
            
            s[left], s[right] = s[right], s[left]
            helper(left+1, right-1)
        helper(0, len(s)-1)

