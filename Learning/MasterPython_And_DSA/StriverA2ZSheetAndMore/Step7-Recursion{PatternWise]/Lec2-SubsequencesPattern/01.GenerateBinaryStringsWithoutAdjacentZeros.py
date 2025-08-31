'''

'''


# Solution 1 Interative

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ['0','1']

        if n == 1:
            return res
        for i in range(2,n+1):
            temp = []
            for j in range(0,len(res)):
                if res[j][-1] == "1":
                    temp.append(res[j]+"0")
                    temp.append(res[j]+"1")
                else:
                    temp.append(res[j]+"1")

                

            res = temp
        return res
    

# Soilution 2 Recursive 

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        self.solve(n,"",res)
        return res
    
    def solve(self, n: int, curr: str, res: List[int])->None:
        if n == 0:
            res.append(curr)
            return
        self.solve(n-1,curr+"1", res)
        if len(curr) == 0 or curr[-1]== "1":
            self.solve(n-1,curr+"0",res)