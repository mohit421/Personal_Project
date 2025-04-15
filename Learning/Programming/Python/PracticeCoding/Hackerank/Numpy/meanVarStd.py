# Sol 1

import numpy

N,M = map(int,input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(N)])

print(numpy.mean(arr,axis = 1))
print(numpy.var(arr,axis = 0))
print(round(numpy.std(arr,axis = None),11))

# Solution 2   Using unpacking and list comprehension (no axis usage)


import numpy as np

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
arr = np.array(data)

# Mean along rows (axis=1)
row_means = [np.mean(row) for row in arr]
print(np.array(row_means))

# Variance along columns (axis=0)
cols = zip(*data)
col_vars = [np.var(list(col)) for col in cols]
print(np.array(col_vars))

# Std of entire array
print(np.std(arr))


# vSolution 3: Fully Manual (no NumPy)

import math

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Mean along rows
means = [sum(row) / m for row in matrix]
print(means)

# Variance along columns
cols = list(zip(*matrix))
vars_ = [sum((x - sum(col)/n)**2 for x in col) / n for col in cols]
print(vars_)

# Std of all values
flat = [x for row in matrix for x in row]
mean_all = sum(flat) / len(flat)
std = math.sqrt(sum((x - mean_all)**2 for x in flat) / len(flat))
print(std)

