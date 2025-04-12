import numpy

N,M,P = map(int,input().split())

arrN = numpy.array([input().split() for _ in range(N)],int)
arrM = numpy.array([input().split() for _ in range(M)],int)

arrConcat = numpy.concatenate((arrN,arrM)) 
arrConcat.shape = ((N+M),P) 

print(arrConcat)