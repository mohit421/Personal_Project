'''

'''


# Brute force approach
'''
Time Complexity: O(n³)
O(n²) substrings.

O(n) to check if each is a palindrome.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    if len(substr) > max_len:
                        max_len = len(substr)
                        longest = substr
        return longest
    


# Optimised one

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest = ""

        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    longest = s[l:r+1]
                    max_len = r-l+1
                l -= 1
                r += 1
            
            l,r = i,i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    longest = s[l:r+1]
                    max_len = r-l+1
                l -= 1
                r += 1
        return longest
    

# Another ways
'''
 Time and Space Complexity:
Time: O(n²)

Space: O(1) (only a few variables used, no extra data structures)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # Final valid palindrome substring

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd = expandAroundCenter(i, i)
            # Even-length palindrome
            even = expandAroundCenter(i, i + 1)
            
            # Update result
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest
