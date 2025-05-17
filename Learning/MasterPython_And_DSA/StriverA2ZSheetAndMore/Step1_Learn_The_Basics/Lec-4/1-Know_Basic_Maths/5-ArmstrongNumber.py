'''
Armstrong Number :- https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1



'''


class Solution:
    def armstrongNumber (self, n):
        # code here 
        s = str(n)
        x = int(s[0])**3 + int(s[1])**3 + int(s[2])**3
        return x==n
    

# Solution 2


class Solution:
    def armstrongNumber (self, n):
        # code here 
        armNum = 0
        temp = n
        while n>0:
           rem = n%10
           armNum += rem**3
           n //= 10
        return temp == armNum