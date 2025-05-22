'''
TC:- O(Q*N)
'''

s = input()

hash = [0]*26
for i in range(len(s)):
    hash[ord(s[i])-ord('a')] += 1

q = int(input())
for _ in range(q):
    c = input()
    print(hash[ord(c)-ord('a')])

