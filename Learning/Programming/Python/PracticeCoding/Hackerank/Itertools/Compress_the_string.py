# Solution 1

from itertools import groupby

s = input()
for k, g in groupby(s):
    print(f"({len(list(g))}, {k})", end=' ')


# Solution 2

from itertools import groupby

s = input()
print(' '.join(f"({len(list(g))}, {k})" for k, g in groupby(s)))


# Solution 3


# Manual Loop Without Any Imports
s = input()
comprStr = []
count = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count+=1
    else:
        comprStr.append(f"({count}, {s[i-1]})")
        count = 1  #reset count
    
comprStr.append(f"({count}, {s[-1]})")

print(*comprStr)