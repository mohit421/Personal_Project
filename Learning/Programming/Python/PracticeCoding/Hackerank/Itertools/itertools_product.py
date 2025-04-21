from itertools import product
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(list(product(A,B)))


# soltuion 2

# Read input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute Cartesian Product manually
cartesian_product = []

for a in A:
    for b in B:
        cartesian_product.append((a, b))

# Print result
print(*cartesian_product)

# solution 3

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = [(a, b) for a in A for b in B]
print(*result)


# solution 4

import numpy as np

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = np.array(np.meshgrid(A, B)).T.reshape(-1, 2)
print(*map(tuple, result))
