import numpy as np

# Read input
N = int(input())
A = np.array([list(map(int, input().split())) for _ in range(N)])
B = np.array([list(map(int, input().split())) for _ in range(N)])

# Matrix multiplication
result = np.matmul(A, B)
# result = np.dot(A, B)

print(result)
