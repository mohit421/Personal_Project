'''

'''


class Solution(object):
    def revStr(self, i, s):
        n = len(s)
        if i >= n // 2:
            return s
        s[i], s[n - i - 1] = s[n - i - 1], s[i]
        return self.revStr(i + 1, s)

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = [c.lower() for c in s if c.isalnum()]
        reversed_s = self.revStr(0, cleaned[:])
        return cleaned == reversed_s


# Solution 2

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
    

# Solution 3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]     
    



'''''other'''
class Solution(object):
    i = 0
    def isPalindrome(self,i, s):
        """
        :type s: str
        :rtype: bool
        """
        if i> len(s)//2:
            return True
        if s[i]  != s[len(s) - i - 1]:
            return False
        return isPlaindrome(i+1,s)
