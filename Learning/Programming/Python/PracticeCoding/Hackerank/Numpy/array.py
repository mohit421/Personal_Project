import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    ans = numpy.array(arr,float)
    return ans

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# Solution 2  One-liner inside function

import numpy as np

def arrays(arr):
    return np.array([float(x) for x in arr[::-1]])

arr = input().strip().split()
print(arrays(arr))


# Solution 3  Basic NumPy (Using numpy.array + slicing)

import numpy as np

def arrays(arr):
    return np.array(arr[::-1], float)

arr = input().strip().split()
result = arrays(arr)
print(result)
