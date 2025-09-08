'''

'''

# Solution 1   Brian Kernighan’s Algorithm (Most Efficient)
'''
⏱️ Time Complexity: O(number of set bits)
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while n:
            n = n&(n-1)
            cnt += 1

        return cnt
    

# Solution 2  Bit by Bit Checking

'''
Time Complexity: O(total bits)
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while n:
            cnt += n&1
            n = n>>1

        return cnt
    

# Python built-in
'''
Step 1: bin(n)

bin(n) converts the number into a binary string.

For example: bin(13) → "0b1101".

This takes O(log n) time because the binary representation has about log₂(n) bits.

Step 2: .count("1")

This scans the string and counts how many '1' characters exist.

The string length is also O(log n).

So, .count("1") runs in O(log n) time.

O(log n) + O(log n) = O(log n)

'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")  
    
#  Python 3.10+

class Solution:
    def hammingWeight(self, n: int) -> int:
        return (n).bit_count()


# Brute force

'''

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n>1:
            if n%2==1:
                cnt += 1
            n = n//2
        if n == 1:
            cnt +=1 
        return cnt
    

# COnvert above into bit manipulation


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n>1:
            if n%2==1:
                cnt += n&1
            n = n>>1
        if n == 1:
            cnt +=1 
        return cnt
    
    
    
    