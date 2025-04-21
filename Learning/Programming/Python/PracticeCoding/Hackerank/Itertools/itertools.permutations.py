from itertools import permutations

s, k = input().split()
k = int(k)

result = list(map(lambda x: ''.join(x), permutations(sorted(s), int(k))))
print(*sorted(result), sep='\n')


# solution  2

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

S,k = input().split()
k = int(k)
# print(list(permutations(S,k)))
for p in sorted(permutations(sorted(S),k)):
    print(''.join(p))