'''
Print ALl Divisor :- https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1

'''

# Solution 1 Brute force
'''

'''

class Solution:
    def print_divisors(self, N):
        # code here
        l = []
        for i in range(1,N+1):
            if N%i==0:
                l.append(i)
        ls = sorted(l)
        for i in ls:
            print(i, end= ' ')


# SOlution 2  Optimised Solution

'''
Algorithm

Step 1: Initialise an array to store the divisors.

Step 2: Iterate from 1 to square root of n using a loop variable ‘i’. For each value of ‘i’:

Check if ‘i’ is a divisor of ‘n’ by checking if ‘n’ is divisible by ‘i’ without a remainder (‘n’%i == 0).
If i is a divisor, add it to the vectors of divisors.
If i is different from n/i add the counterpart divisor n/i to the vector of divisors.

'''

'''
TC:- O(no of factor *log(no of factor)) + O(sqrt(n))
'''
import math
class Solution:
    def print_divisors(self, N):
        # code here
        l = []
        sqt = int(math.sqrt(N))
        for i in range(1,sqt+1):
            if N%i==0:
                l.append(i)
                if i != N//i:
                    l.append(N//i)
        l = sorted(l)
        for i in l:
            print(i,end=' ')

# Solution 3
import math
class Solution:
    def print_divisors(self, N):
        # code here
        s,l = [],[]
        sqt = int(math.sqrt(N))
        for i in range(1,sqt+1):
            if N%i==0:
                s.append(i)
                if i != N//i:
                    l.append(N//i)
        print(*(s +l[::-1]),end='')


# Solution 4  List comprehsension

import math
class Solution:
    def print_divisors(self, N):
        # code here
        divisor = [i for i in range(1,int(N**0.5)+1) if N%i==0]
        mirror = [N//i for i in divisor if i!=N//i]
        print(*(sorted(divisor + mirror)),end='')