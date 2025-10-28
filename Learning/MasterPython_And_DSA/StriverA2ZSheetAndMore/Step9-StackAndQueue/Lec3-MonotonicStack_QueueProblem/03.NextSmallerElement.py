'''

'''
# Soilution 1 Brute force


class Solution:
	def nextSmallerEle(self, arr):
		# code here
		n = len(arr)

        # Initialize the result array with -1
        ans = [-1] * n

        # Traverse each element
        for i in range(n):
            # Check subsequent elements for smaller value
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    # Store and break on first smaller element
                    ans[i] = arr[j]
                    break

        # Return the result array
        return ans


# SOlution 2  optimized approach

class Solution:
	def nextSmallerEle(self, arr):
		# code here
		n = len(arr)
        if n == 0:
            return []
        res = [-1] * n
        st = []
        
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                idx = st.pop()
                res[idx] = arr[i]
            
            if i < n:
                st.append(i)
        
        return res