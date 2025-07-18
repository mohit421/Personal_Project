'''
Find the Nth root of a number using binary search

'''



# Solution 1 Brute force

#User function Template for python3
'''
Complexity Analysis

Time Complexity: O(M), M = the given number.
Reason: Since we are using linear search, we traverse the entire answer space.

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    
    def func(self,b, exp):
        ans = 1
        base = b
        while exp > 0:
            if exp % 2:
                exp -= 1
                ans = ans * base
            else:
                exp //= 2
                base = base * base
        return ans
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
		for i in range(1, m + 1):
            val = self.func(i, n)
            if val == m:
                return i
            elif val > m:
                break
        return -1


# Other ways using brute force
#User function Template for python3

class Solution:
    
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
		for i in range(1, m + 1):
            val = i**n
            if val == m:
                return i
            elif val > m:
                break
        return -1

# Solution 2 Optimised one using binary search
#User function Template for python3

class Solution:
    
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
		lo,hi = 1, m
		
		while lo<=hi:
		    mid = (lo+hi)//2
		    if mid**n == m:
		        return  mid
		    if mid**n>m:
		        hi = mid-1
		    else:
		        lo = mid+1
		return -1



# Striver solution



def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)
