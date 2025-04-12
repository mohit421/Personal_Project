import numpy
def trans(arr):
    lst = numpy.array(arr,dtype =int)
    print(numpy.transpose(lst))
    print(lst.flatten())

N,M = list(map(int,input().strip().split()))
arr = []

for j in range(N):
        arr.append(input().rstrip().split())
trans(arr)



# Solution 2

import numpy

N,M = map(int, input().split())

arr = numpy.array([input().split() for _ in range(N)],int)
print(arr.T)
print(arr.flatten())
