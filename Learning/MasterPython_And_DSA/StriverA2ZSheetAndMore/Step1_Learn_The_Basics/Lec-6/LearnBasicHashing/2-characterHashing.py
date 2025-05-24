'''
TC:- O(Q*N)
'''

# Input the string
s = input()

# Precompute frequency of each lowercase letter
hash_array = [0] * 26
for ch in s:
    hash_array[ord(ch) - ord('a')] += 1

# Input number of queries
q = int(input())
for _ in range(q):
    c = input()
    print(hash_array[ord(c) - ord('a')])
