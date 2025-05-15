'''
****
****
****
****

'''

'''
0 - 4 star
1- 4 star
3- 4 start
4 - 4 star
'''

# n = 4
# for i in range(n):
#     for j in range(n):
#         print('*', end=" ")
#     print()


def print1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
