'''
Link:- https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1
Problem:- Count the number of subarrays with given xor K
'''

# Solution 1 Brute force
'''
omplexity Analysis

Time Complexity: O(N3) approx., where N = size of the array.
Reason: We are using three nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i,n):
                xor = 0
                for l in range(i,j+1):
                    xor = xor ^ arr[l]
                if xor == k:
                    cnt += 1
        return cnt
    

# SOlution 2 Better solutton 

'''
Time Complexity: O(N2), where N = size of the array.
Reason: We are using two nested loops here. As each of them is running for N times, the time complexity will be approximately O(N2).

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        n = len(arr)
        cnt = 0
        for i in range(n):
            xor = 0
            for j in range(i,n):
                xor = xor ^ arr[j]
                if xor == k:
                    cnt += 1
        return cnt



# Solution 3 Optimized Solution 
'''
Complexity Analysis

Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array. Point to remember for unordered_map in the worst case, the searching time increases to O(N), and hence the overall time complexity increases to O(N2). 

Space Complexity: O(N) as we are using a map data structure.
'''
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        n = len(arr)
        cnt = 0
        dic = {}
        preXor = 0
        dic[preXor] = 1
        for i in range(n):
            preXor = preXor ^ arr[i]
            rem = preXor ^ k
            cnt += dic.get(rem,0)
            dic[preXor] = dic.get(preXor,0) + 1
        
        return cnt
