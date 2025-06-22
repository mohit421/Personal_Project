'''
Problem Link:- https://leetcode.com/problems/single-number/description/


Find the number that appears once, and other numbers twice.
'''


# Solution 1  Brute force approach

'''
Complexity Analysis

Time Complexity: O(N2), where N = size of the given array.
Reason: For every element, we are performing a linear search to count its occurrence. The linear search takes O(N) time complexity. And there are N elements in the array. So, the total time complexity will be O(N2).

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            cnt = 0
            num = nums[i]
            for j in range(n):
                if nums[j] == num:
                    cnt += 1
            if cnt == 1:
                return num
        return -1


    


# Solution 2 Better solution 
'''
Complexity Analysis

Time Complexity: O(N)+O(N)+O(N), where N = size of the array
Reason: One O(N) is for finding the maximum, the second one is to hash the elements and the third one is to search the single element in the array.

Space Complexity: O(maxElement+1) where maxElement = the maximum element of the array.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        offset = abs(min(nums)) if min(nums)<0 else 0
        size = max(nums) +  offset + 1
        hash = [0]*size
        for num in nums:
            hash[num+offset] += 1
        for num in nums:
            if hash[num+offset]==1:
                return num
        return -1


    
# Solution 3

'''


User
Toggle Sidebar

DSA Sheet

DSA Playlist

Core Subjects

Others
TUF Dark
Unlock personalized learning and exclusive roadmaps.
Explore Plans
Premium Icon
Get Plus
Find the number that appears once, and the other numbers twice

Mark as Completed

373


Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

Examples
Disclaimer: Don’t jump directly to the solution, try it out yourself first.

Brute Force Approach
Algorithm / Intuition
Naive Approach(Brute-force approach): 
Intuition:
For every element present in the array, we will do a linear search and count the occurrence. If for any element, the occurrence is 1, we will return it.

Approach:
The steps are as follows:

First, we will run a loop(say i) to select the elements of the array one by one.
For every element arr[i], we will perform a linear search using another loop and count its occurrence.
If for any element the occurrence is 1, we will return it.
Code
C++
Java
Python
JavaScript





def getSingleElement(arr):
    # Size of the array:
    n = len(arr)

    # Run a loop for selecting elements:
    for i in range(n):
        num = arr[i]  # selected element
        cnt = 0

        # Find the occurrence using linear search:
        for j in range(n):
            if arr[j] == num:
                cnt += 1

        # If the occurrence is 1, return the number:
        if cnt == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)


if __name__ == '__main__':
    main()


Output: The single element is: 4

Complexity Analysis

Time Complexity: O(N2), where N = size of the given array.
Reason: For every element, we are performing a linear search to count its occurrence. The linear search takes O(N) time complexity. And there are N elements in the array. So, the total time complexity will be O(N2).

Space Complexity: O(1) as we are not using any extra space.

Better Approach 1
Algorithm / Intuition
Better Approach(Using Hashing): 
Intuition:
In the previous approach, we were finding the occurrence of an element using linear search. We can optimize this using hashing technique. We can simply hash the elements along with their occurrences in the form of (key, value) pair. Thus, we can reduce the cost of finding the occurrence and hence the time complexity.

Now, hashing can be done in two different ways and they are the following:

Array hashing(not applicable if the array contains negatives or very large numbers)
Hashing using the map data structure
Array hashing:
In order to hash using an array, we need to first find the maximum element(say maxElement) to get the range of the hash array. The index of the hash array will represent the elements of the given array and the value stored in that index will be the number of occurrences. Now, the size of the array must be maxElement+1 as we need to hash the maxElement itself.

Approach:

The steps are as follows:

First, we will find the maximum element(say maxElement) to know the size of the hash array.
Then we will declare a hash array of size maxElement+1.
Now, using another loop we will store the elements of the array along with their frequency in the hash array. (i.e. hash[arr[i]]++)
After that, using another loop we will iterate over the hash array, and try to find the element for which the frequency is 1, and finally, we will return that particular element.
Note: While searching for the answer finally, we can either use a loop from 0 to n(i.e. Size of the array) or use a loop from 0 to maxElement. So, the time complexity will change accordingly.

Now, using array hashing it is difficult to hash the elements of the array if it contains negative numbers or a very large number. So to avoid these problems, we will be using the map data structure to hash the array elements.

Code
C++
Java
Python
JavaScript





def getSingleElement(arr):
    # Size of the array:
    n = len(arr)

    # Find the maximum element:
    maxi = max(arr)

    # Declare hash array of size maxi+1
    # And hash the given array:
    hash = [0] * (maxi + 1)
    for num in arr:
        hash[num] += 1

    # Find the single element and return the answer:
    for num in arr:
        if hash[num] == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)


if __name__ == '__main__':
    main()



Output: The single element is: 4

Complexity Analysis

Time Complexity: O(N)+O(N)+O(N), where N = size of the array
Reason: One O(N) is for finding the maximum, the second one is to hash the elements and the third one is to search the single element in the array.

Space Complexity: O(maxElement+1) where maxElement = the maximum element of the array.

Better Approach 2
Algorithm / Intuition
Hashing using the map data structure: 
Intuition:
The intuition will be the same as the array hashing. The only difference here is we will use the map data structure for hashing instead of using another array for hashing.

Approach:
The steps are as follows:

First, we will declare a map.
Now, using a loop we will store the elements of the array along with their frequency in the map data structure.
Using another loop we will iterate over the map, and try to find the element for which the frequency is 1, and finally, we will return that particular element.
Code
C++
Java
Python
JavaScript





def get_single_element(arr):
    # Size of the array:
    n = len(arr)

    # Declare the hashmap.
    # And hash the given array:
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1

    # Find the single element and return the answer:
    for num, count in hashmap.items():
        if count == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = get_single_element(arr)
    print("The single element is:", ans)


if __name__ == "__main__":
    main()



Output: The single element is: 4

Complexity Analysis

Time Complexity: O(N*logM) + O(M), where M = size of the map i.e. M = (N/2)+1. N = size of the array.
Reason: We are inserting N elements in the map data structure and insertion takes logM time(where M = size of the map). So this results in the first term O(N*logM). The second term is to iterate the map and search the single element. In Java, HashMap generally takes O(1) time complexity for insertion and search. In that case, the time complexity will be O(N) + O(M).

Note: The time complexity will be changed depending on which map data structure we are using. If we use unordered_map in C++, the time complexity will be O(N) for the best and average case instead of O(N*logM). But in the worst case(which rarely happens), it will be nearly O(N2).

Space Complexity: O(M) as we are using a map data structure. Here M = size of the map i.e. M = (N/2)+1.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        
        for num, count in hashmap.items():
            if count == 1:
                return num
        return -1


    


# ?Solution 4  Optimised one using xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        xor1 = 0
        for i in range(N):
            xor1 ^= nums[i]
        return xor1