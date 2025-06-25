'''
Link:- https://leetcode.com/problems/majority-element/

'''

# Solution 1   Brute force Approach
'''
Complexity Analysis
Time Complexity: O(N2), where N = size of the given array. Reason: For every element of the array the inner loop runs for N times. And there are N elements in the array. So, the total time complexity is O(N2). Space Complexity: O(1) as we use no extra space.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    cnt += 1
            if n//2<cnt:
                return nums[i]
        return -1

        




# SOlution 2 use Hashing


'''

 Time Complexity: O(n)
The for i in nums loop runs in O(n) time.

The for i in di loop runs in O(k) time, where k is the number of unique elements.
But in the worst case, k = n (if all elements are unique).

So overall: O(n + k) = O(n)

🧠 Space Complexity: O(n)
The dictionary di stores up to n keys (in worst case, all elements are unique).

So space usage grows linearly with input size.

Summary:
Metric	Complexity
Time	O(n)
Space	O(n)
'''
'''
Solution 2 (Better):
Intuition:
Use a better data structure to reduce the number of look-up operations and hence the time complexity. Moreover, we have been calculating the count of the same element again and again - so we have to reduce that also.

Approach: 
Use a hashmap and store as (key, value) pairs. (Can also use frequency array based on the size of nums) 
Here the key will be the element of the array and the value will be the number of times it occurs. 
Traverse the array and update the value of the key. Simultaneously check if the value is greater than the floor of N/2. 
If yes, return the key 
Else iterate forward.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di = {}
        for i in nums:
            di[i] = di.get(i, 0) + 1 
        for i in nums:
            if di[i]> len(nums)//2:
                return i
        return -1
        

# Solution 2.1 using counter builtin func
'''
Time Complexity: O(N*logN) + O(N), where N = size of the given array.
Reason: We are using a map data structure. Insertion in the map takes logN time. And we are doing it for N elements. So, it results in the first term O(N*logN). The second O(N) is for checking which element occurs more than floor(N/2) times. If we use unordered_map instead, the first term will be O(N) for the best and average case and for the worst case, it will be O(N2).

Space Complexity: O(N) as we are using a map data structure.
'''
'''
Time Complexity: O(n)
Breakdown:

Counter(nums) — This scans the list once and counts frequencies.
✅ Time: O(n)

for num, count in counter.items() — Iterates through up to n items (worst case: all unique).
✅ Time: O(n)

Inside the loop: len(nums) // 2 < count — Constant time comparison.
✅ Time: O(1) per iteration

So total time complexity:

Space Complexity: O(n)
Counter creates a dictionary with up to n keys (in worst case, all elements are unique).

So space used is linear in the size of the input.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Count the occurrences of each element using Counter
        counter = Counter(nums)
        # Searching for the majority element
        for num,count in counter.items():
            if len(nums)//2 < count:
                return num
        return -1



# Solution 3 Optimised solution uisng Moore's Voting Algorithm

'''
Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the count and find the expected majority element. The second one is to check if the expected element is the majority one or not.

Note: If the question states that the array must contain a majority element, in that case, we do not need the second check. Then the time complexity will boil down to O(N).

Space Complexity: O(1) as we are not using any extra space.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        el = 0
        for i in nums:
            if cnt == 0:
                cnt = 1
                el = i
            elif i == el:
                cnt += 1
            else:
                cnt -= 1
        cnt1 = 0
        for i in nums:
            if el == i:
                cnt1 += 1
        if cnt1 > len(nums)//2:
            return el
        

