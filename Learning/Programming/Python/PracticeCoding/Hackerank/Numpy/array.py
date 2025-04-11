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