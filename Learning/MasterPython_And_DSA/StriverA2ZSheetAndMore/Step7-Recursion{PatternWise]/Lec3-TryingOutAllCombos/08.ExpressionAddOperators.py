'''


'''


# Solution 1

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def expression(i,s1, sum1, last):
            if i>=len(num):
                if sum1 == target:
                    ans.append(s1)
                return
            
            for j in range(i,len(num)):
                if j>i and num[i] == '0':
                    return
                curr = int(num[i:j+1])
                if i == 0:
                    expression(j+1, s1+str(curr),curr, curr)
                else:
                    expression(j+1,s1+ "+" + str(curr), sum1+curr, curr)
                    expression(j+1,s1+ "-" + str(curr), sum1-curr, -curr)
                    expression(j+1,s1+ "*" + str(curr), sum1 -last +(curr*last), curr*last)

            
        
        expression(0,"",0,0)
        return ans