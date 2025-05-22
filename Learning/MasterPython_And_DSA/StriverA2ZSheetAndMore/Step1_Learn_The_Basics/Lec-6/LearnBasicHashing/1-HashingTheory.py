# Brute force
'''
TC:- O(Q*N)

lets say Q= 10^5
and N = 10^5
so TC:- 10^10
10^8 => 1s
10^10 => 100s

that's why hashing comes in
for theory read BasicHashing.md file

'''

# def nonHashingWay(num,ar):
#     cnt= 0
#     n = len(ar)
#     for i in range(n):
#         if ar[i] == num:
#             cnt += 1

#     return cnt 

# num = int(input())
# ar = list(map(int,input().split()))

# print(nonHashingWay(num,ar))



# Hashing ways




if __name__=="__main__":
    n = int(input('Give me number of input: -'))
    arr = list(map(int,input("give me number in arr: ").split()))
    hash = [0]*13
    for i in arr:
        hash[i] += 1
    q = int(input("your total query: "))
    for _ in range(q):
        num = int(input("your query input: "))
        print(hash[num])