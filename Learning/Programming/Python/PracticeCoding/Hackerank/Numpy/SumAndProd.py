import numpy



N,M = map(int,input().split())

arr = numpy.array([list(map(int, input().split())) for _ in range(N)])
sm = numpy.sum(arr,axis=0)
print(numpy.prod(sm))