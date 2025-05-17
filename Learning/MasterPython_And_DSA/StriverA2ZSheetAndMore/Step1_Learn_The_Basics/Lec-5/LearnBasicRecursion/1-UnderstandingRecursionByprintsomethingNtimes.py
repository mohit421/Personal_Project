'''
 line 9, in recurSion
    recurSion()
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded  

'''

# Infinite case

'''
def recurSion():
    print(1)
    recurSion()


recurSion()


# Link for notes:- https://takeuforward.org/recursion/introduction-to-recursion-understand-recursion-by-printing-something-n-times/
'''


def recr(cnt):
    if cnt==4:
        return 
    print(cnt)
    cnt += 1
    recr(cnt)
# cnt = 0
recr(0)


