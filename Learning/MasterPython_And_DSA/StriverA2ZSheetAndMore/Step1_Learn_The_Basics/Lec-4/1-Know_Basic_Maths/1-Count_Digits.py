'''
COunt Digits- https://www.geeksforgeeks.org/problems/count-digits5716/0

'''


# Solution 1: Without Converting to String (Mathematical Approach)
class Solution:
    def evenlyDivides(self, n):
        # code here
        count = 0
        temp = n
        while temp>0:
            rem = temp%10
            if rem != 0 and n%rem == 0:
                count += 1
            temp //= 10
        return count


# Solution 2  Simple Iteration with String Conversion

class Solution:
    def evenlyDivides(self, n):
        # code here
        count = 0
        for d in str(n):
            if d != '0' and n % int(d)==0:
                count += 1
        return count
    

# Solution 3  Using List comprehension

def evenlyDivides(self, n):
    # code here
    return sum(1 for d in str(n) if d != '0' and n % int(d) == 0)
    


# Solution 4  Using filter() and lambda


class Solution:
    def evenlyDivides(self, n):
        # code here
        return len(list(filter(lambda d: d != 0 and n % d==0, [int(x) for x in str(n)])))

# Solution 5 Using Recusion

class Solution:
    def evenlyDivides(self, n):
        # code here
        def helper(num):
            if num==0:
                return 0
            d = num%10
            return ((d != 0 and n%d == 0 ) + helper(num//10))
        return helper(n)
    