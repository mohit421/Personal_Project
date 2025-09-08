'''

'''


# SOlution 1

#User function Template for python3
class Solution:
	def setBit(self, n):
		# code here
		
		ans = n
		i = 0
		while n:
		    if n&1==0:
		        break
		    i += 1
		    n >>= 1
        
        return ans | 1<<i

# Solution 2

#User function Template for python3
''''
🕒 Time Complexity

Bitwise OR and addition are O(1) operations.

So the overall time complexity = O(1).


Why does this work?

Adding 1 to a number flips the rightmost 0 bit into 1 and makes all bits to its right into 0.

OR (|) with the original number sets that bit in the original n.


n       = 10  → 1010 (binary)
n + 1   = 11  → 1011
n | n+1 = 1010 | 1011 = 1011 → 11


n       = 7   → 0111
n + 1   = 8   → 1000
n | n+1 = 0111 | 1000 = 1111 → 15

'''
class Solution:
	def setBit(self, n):
		# code here
		
		n = n | (n+1)
        return n
		        
		        