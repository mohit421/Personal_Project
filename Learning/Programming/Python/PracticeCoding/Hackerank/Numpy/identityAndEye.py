# Enter your code here. Read input from STDIN. Print output to STDOUT


import numpy

numpy.set_printoptions(legacy='1.13')

N,M = map(int,input().split())
print(numpy.eye(N,M,k=0))
