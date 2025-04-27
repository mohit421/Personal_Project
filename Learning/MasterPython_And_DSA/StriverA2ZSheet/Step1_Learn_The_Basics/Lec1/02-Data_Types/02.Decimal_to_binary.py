

# Solution 1

class Solution:
    def decToBinary(self, n):
        # code here
        return (bin(n)[2:])
    

# Solution 2

class Solution:
    def decToBinary(self, n):
        # code here
        binary = format(n, 'b')  # '1010'
        return binary

# Soltion 3
class Solution:
    def decToBinary(self, n):
        # code here
        binary2 = f"{n:b}"   
        return binary2