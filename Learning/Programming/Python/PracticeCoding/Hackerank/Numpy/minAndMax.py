import numpy

N,M = map(int,input().split())
arr = numpy.array([list(map(int,input().split())) for _ in range(N)])

mnarr = numpy.min(arr,axis=1)
mxarr = numpy.max(mnarr)
print(mxarr)

