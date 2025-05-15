'''
# Palindrome Number:- https://leetcode.com/problems/palindrome-number/description/

'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        


# Solution 2 Without using string conversion

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        rev = 0
        temp = x
        while x>0:
            rem = x%10
            x //= 10
            rev = rev*10 + rem
        if temp == rev:
            return True
        return False
    

# Solution 3

def isPalindrome(x):
    return str(x) == str(x)[::-1]



# Solution 4   Without String Conversion (Reversing Half of the Number)


def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10
