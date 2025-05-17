'''
Print name N times using Recursion


'''

# def name(nm,cnt):
#     print(nm)
#     if cnt == 4:
#         return
#     cnt += 1
#     name(nm,cnt)
# cnt = 0
# nm = "mohit jaiswal"
# name(nm,cnt)


# Solution 2
'''
TC:- O(N)
SC:- O(N)
'''
def func(i,n):
    if i>n:
        return
    print("Mohit Jaiswal")
    func(i+1,n)

n = int(input())
func(1,n)