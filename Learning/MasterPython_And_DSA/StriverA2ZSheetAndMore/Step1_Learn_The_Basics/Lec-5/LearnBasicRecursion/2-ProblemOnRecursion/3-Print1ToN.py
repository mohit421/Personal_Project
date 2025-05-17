'''
Print :- N...1
'''


def print1N(i,N):
    
    if i<1:
        return
    print(i)
    print1N(i-1,N)
    

N = int(input())
print1N(N,N)

# Print 1 to N using backtrack

# def print1N(i,N):
    
#     if i>N:
#         return
#     print1N(i+1,N)
#     print(i)

# N = int(input())
# print1N(1,N)