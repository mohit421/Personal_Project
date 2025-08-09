'''

'''

# Solution1 
'''
TC:- O(N)
SC:- O(1)
'''
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[:i+1]
        return ""


# Using while loop

def largestOddNumber(self, num: str) -> str:
	i = len(num) - 1
	while i >= 0:
		if int(num[i]) % 2:
			return num[:i + 1]
		i-= 1

	return ""


# Another approach

class Solution:
    def largestOddNumber(self, num: str) -> str:
        right = len(num) - 1
        while (right >= 0) and (int(num[right]) & 1) == 0:
            right -= 1
        return num[:right+1]