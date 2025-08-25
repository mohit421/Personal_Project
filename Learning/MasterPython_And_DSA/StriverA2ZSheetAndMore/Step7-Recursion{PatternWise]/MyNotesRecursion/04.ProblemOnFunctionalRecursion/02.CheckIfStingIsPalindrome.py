'''
Check if a string is palindrome
'''


class Solution:
    def check(self, s: str, i:int):
        n = len(s)
        if i>=n//2:
            return True
        if s[i] != s[n-i-1]:
            return False
        return self.check(s,i+1)

    def isPalindrome(self, s: str) -> bool:
        # Preprocess string: keep only alphanumeric, lowercase
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
        return self.check(filtered, 0)
