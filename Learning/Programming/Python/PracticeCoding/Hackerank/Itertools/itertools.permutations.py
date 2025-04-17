from itertools import permutations

s, k = input().split()
k = int(k)

result = list(map(lambda x: ''.join(x), permutations(sorted(s), int(k))))
print(*sorted(result), sep='\n')