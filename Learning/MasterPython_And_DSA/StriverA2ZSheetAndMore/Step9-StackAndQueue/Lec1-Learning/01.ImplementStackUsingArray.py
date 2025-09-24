'''
Implement Stack using Arrays
'''

# Solution
'''
Time Complexity: O(N)

Space Complexity: O(N)
'''
class MyStack:
    def __init__(self):
        self.size = 1000
        self.arr=[-1]*self.size
        self.top = -1
        
    
    def push(self,data):
        #add code here
        self.top += 1
        self.arr[self.top] = data
    
    def pop(self):
        #add code here
        data = self.arr[self.top]
        self.top -= 1
        return data
        
        