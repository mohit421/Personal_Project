'''
7. Reverse Integer:- https://leetcode.com/problems/reverse-integer/description/?envType=problem-list-v2&envId=math

'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            result = -1 * int(str(abs(x))[::-1])
        else:
            result = int(str(x)[::-1])
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
        



# Solution 2

class Solution(object):
    def revStr(self,x):
        rev = 0
        while x>0:
            rem = x%10
            x //= 10
            rev = rev*10 + rem
        return rev


    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            # result = -1 * int(str(abs(x))[::-1])
            result = -1 * self.revStr(abs(x))
        else:
            result = self.revStr(x)
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result


# Solution 3  

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = int(str(abs(x))[::-1])*(-1 if x<0 else 1)
        return rev if -2**31<=rev<=2**31-1 else 0
    

# Solution 4  Using List and Join (Alternative Pythonic)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0]=='-':
            rev = int('-' + ''.join(reversed(s[1:])))
        else:
            rev = int(''.join(reversed(s)))
        return rev if -2**31<=rev<=2**31-1 else 0
    
# Solution 5  Math Approach

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x != 0:
            d = x%10
            x = x//10
            res = res*10 + d
        res *= sign

        return res if -2**31<=res<=2**31-1 else 0
    

# Solution 6  String Conversion Method (Most Pythonic)

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1]) * sign
        return rev if -2**31 <= rev <= 2**31 - 1 else 0