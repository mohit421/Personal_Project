# Designer Door Mat 
# Problem Link :- https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

N,M = map(int, input().split())
for i in range(1,N,2):
    print((".|."*i).center(M,'-'))
print("WELCOME".center(M,'-'))

for i in range(N-2,-1,-2):
    print(('.|.'*i).center(M,'-'))



# Code 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
#  Using List Comprehension

N,M = map(int, input().split())

patt = [(".|."*i).center(M,'-') for i in range(1,N,2)]
print('\n'.join(patt+ ["WELCOME".center(M,'-')] + patt[::-1]))

    
# Code 3
# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M = map(int, input().split())

patt = ['{:-^{}}'.format(".|."*i,M) for i in range(1,N,2)]
print('\n'.join(patt+ ['{:-^{}}'.format("WELCOME",M)] + patt[::-1]))

    
# Code 4

N, M = map(int, input().split())

for i in range(1, N, 2):
    print('{:-^{}}'.format('.|.' * i, M))
print('{:-^{}}'.format('WELCOME', M))
for i in range(N-2, 0, -2):
    print('{:-^{}}'.format('.|.' * i, M))


# Code 4

import itertools

N, M = map(int, input().split())

top = [('.|.' * i).center(M, '-') for i in range(1, N, 2)]
middle = ['WELCOME'.center(M, '-')]
bottom = top[::-1]

print('\n'.join(itertools.chain(top, middle, bottom)))