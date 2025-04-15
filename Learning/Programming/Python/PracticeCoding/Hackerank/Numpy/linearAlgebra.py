# Solution 1

import numpy as np

n = int(input())
matrix = [list(map(float, input().split())) for _ in range(n)]

det = np.linalg.det(matrix)
print(round(det, 2))


# Solution 2
from sympy import Matrix

n = int(input())
matrix = [list(map(float, input().split())) for _ in range(n)]

det = Matrix(matrix).det()
print(round(float(det), 2))
