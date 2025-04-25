# DefaultDict -> Collections
# Solution 1
'''
defaultdict(list) makes it easy to group indices of same words.

For each word in Group A, you store its 1-based position.

For each word in Group B, print positions if found, else -1.
'''

from collections import defaultdict

d = defaultdict(list)
n,m = map(int,input().split())
A = [input().strip() for _ in range(n)]
B = [input().strip() for _ in range(m)]

for i, word in enumerate(A):
    d[word].append(i+1)

for word in B:
    if word in d:
        print(' '.join(map(str,d[word])))
    else:
        print(-1)


# Solution 2
# Solution 2: Using itertools.groupby (less conventional)

# from itertools import groupby


n,m = map(int,input().split())
A = [input().strip() for _ in range(n)]
B = [input().strip() for _ in range(m)]

d  = {}
for i, word in enumerate(A):
    d.setdefault(word,[]).append(i+1)

for word in B:
    if word in d:
        print(' '.join(map(str,d[word])))
    else:
        print(-1)