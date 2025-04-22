# Solution 1
'''
Brute Force with itertools.combinations
 Works best for small n (up to ~20)


'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
# engLetters = input().split()
engLetters = list(map(str, input().split()))
k = int(input())
# All possible combinations of indices of size k
all_combinations = list(combinations(range(N),k))

# Filter combinations that contain at least one 'a'

favourables = [comb for comb in all_combinations if 'a' in [engLetters[i] for i in comb]]

# Probability Calculation
probability = len(favourables)/len(all_combinations)
print(f"{probability:.3f}")

# Solutions 2
'''
METHOD 2: Complement Rule using Math (Efficient)
✅ Efficient for large inputs
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def comb(n,r):
    return math.comb(n,r) if n>=r else 0
    
n = int(input())
letters = input().split()
k = int(input())

a_count = letters.count('a')
non_a_count = n - a_count 

total_combination = comb(n,k)
no_a_combination = comb(non_a_count,k)

probability = 1- (no_a_combination/total_combination)

print(f"{probability:.3f}")
    

# Solution 3

'''
METHOD 3: Probability Simulation (Monte Carlo)

'''