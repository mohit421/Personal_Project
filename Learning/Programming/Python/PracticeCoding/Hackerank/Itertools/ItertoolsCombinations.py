# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations


S,k = input().split()
k = int(k)
s= sorted(S)
for i in range(1,k+1):
    for j in sorted(combinations(s,i)):
        print(''.join(j))


# Solution 2

def combinations_generator(s, k):
    if k == 0:
        yield ''
    else:
        for i in range(len(s)):
            for tail in combinations_generator(s[i+1:], k-1):
                yield s[i] + tail

s, k = input().split()
k = int(k)
s = ''.join(sorted(s))

for i in range(1, k+1):
    for comb in combinations_generator(s, i):
        print(comb)

# Solution 3

from itertools import combinations

s, k = input().split()
k = int(k)

s = sorted(s)
for i in range(1, int(k)+1):
    print('\n'.join(map(lambda x: ''.join(x), combinations(s, i))))
