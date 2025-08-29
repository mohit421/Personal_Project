'''

'''


# Recursive solution 
'''
Complexity

Time: O(NO(LogN))
O(log∣n∣) recursive calls.

Space: O(LogN)
O(log∣n∣) call stack (due to recursion depth).
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x,n):
            if x == 0:  return 0
            if n == 0:  return 1

            res = helper(x, n//2)
            res *=res
            return x*res if n%2 else res

        res = helper(x, abs(n))
        return res if n>=0 else 1/res
    


# More better solution thatn above 
'''
0^(-k) (negative exponent with base 0) will crash
Flow:

helper(0, abs(-k)) returns 0 due to if x == 0: return 0.

Then myPow tries 1 / res → 1 / 0 → ZeroDivisionError.
You may want to explicitly handle this:
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            if n < 0:
                raise ZeroDivisionError("0 cannot be raised to a negative power")
            return 0.0
        def helper(x,n):
            # if x == 0:  return 0
            if n == 0:  return 1

            res = helper(x, n//2)
            res *=res
            return x*res if n%2 else res

        res = helper(x, abs(n))
        return res if n>=0 else 1/res