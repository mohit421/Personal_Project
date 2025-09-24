'''

'''

# Solution 


# Without using bit manipulation 


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Convert to binary strings (remove '0b')
        b1 = bin(start)[2:]
        b2 = bin(goal)[2:]
        
        # Pad with leading zeros so both have same length
        max_len = max(len(b1), len(b2))
        b1 = b1.zfill(max_len)
        b2 = b2.zfill(max_len)
        
        # Count mismatched bits
        cnt = 0
        for i in range(max_len):
            if b1[i] != b2[i]:
                cnt += 1
        
        return cnt



# Without bit manipulation

'''
Time Complexity: O(1), The XOR operation between two integers is performed in constant time, O(1). The for loop iterates over a fixed number of bits (32 bits for a standard integer), which is as good as O(1).

Space Complexity: O(1) – Using a couple of variables i.e., constant space.
'''
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_res = start^goal
        cnt = 0
        while xor_res:
            if xor_res != 0:
                cnt += xor_res&1
                xor_res >>= 1
        return cnt