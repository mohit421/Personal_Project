import numpy


nineInt = input().strip().split()
arr = numpy.array(nineInt,int)
# arr.shape = (3,3)
# print(arr)
print(numpy.reshape(arr,(3,3)))


# solutiopn

import numpy as np

arr = np.array(input().split(), int)
print(arr.reshape(3, 3))


# solition 3

import numpy as np

nums = list(map(int, input().split()))
arr = np.array(nums).reshape(3, 3)
print(arr)

# Solution 4

import numpy as np

arr = np.fromstring(input(), dtype=int, sep=' ').reshape(3, 3)
print(arr)


# solution 5

import numpy as np

data = [int(x) for x in input().split()]
arr = np.array(data).reshape(3, 3)
print(arr)


