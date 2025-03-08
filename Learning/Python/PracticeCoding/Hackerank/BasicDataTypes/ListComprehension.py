# Problem Link:- https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # using nested for loop
    # res = []
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i+j+k != n:
    #                 res.append([i,j,k])
    # print(res)
    # using list comprehension
    res = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
    print(res)

