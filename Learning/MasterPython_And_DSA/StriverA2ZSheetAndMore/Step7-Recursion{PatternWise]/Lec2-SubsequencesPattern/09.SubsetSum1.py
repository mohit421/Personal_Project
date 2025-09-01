'''

'''


# Solution 

'''
Time Complexity: O(2^n)+O(2^n log(2^n)). Each index has two ways. You can either pick it up or not pick it. So for n index time complexity for O(2^n) and for sorting it will take (2^n log(2^n)).

Space Complexity: O(2^n) for storing subset sums, since 2^n subsets can be generated for an array of size n.

'''

class Solution:
	def subsetSums(self, arr):
		# code here
		ans = []
		n = len(arr)
		
		def helper(i, sm):
		    if i == n:
		        ans.append(sm)
		        return
	    
	        helper(i+1, sm+arr[i])
            helper(i+1,sm)		    
		   
		helper(0,0)
		return ans