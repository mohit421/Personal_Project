# Problem Link: https://www.geeksforgeeks.org/problems/adam-number2650/1?&selectedLang=python3

# Solution 1
class Solution:
    def checkAdamOrNot(self, N):
        rev = int(str(N)[::-1])
        orig_sqr = N**2
        
        # Step 2: reverse the digits of N and square that
        revSqr = rev**2
        
        # Step 3: reverse the square of N
        revOrig_sqr = str(orig_sqr)[::-1]
        
        # Step 4: Compare
        if revOrig_sqr == str(revSqr):
            return "YES"
        else:
            return "NO"
        

# Solution 2

'''
Without String Reversal  using arithmetic only (Straight forward approach)
'''
# We can't do this for 1120 it got failwed

class Solution:
    def reverse(self, num):
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10
        return rev

    def checkAdamOrNot(self, N):
        # Reverse N and calculate squares
        rev_N = self.reverse(N)
        N_squared = N * N
        rev_N_squared = rev_N * rev_N
        
        # Reverse the squares
        rev_N_squared_rev = self.reverse(N_squared)
        
        return "YES" if rev_N_squared == rev_N_squared_rev else "NO"
