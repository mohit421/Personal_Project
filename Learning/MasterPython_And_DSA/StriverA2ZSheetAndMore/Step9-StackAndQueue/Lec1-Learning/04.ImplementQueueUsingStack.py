'''

'''

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())
        

    def pop(self) -> int:
        if not self.s1:
            return None
        return self.s1.pop()

    def peek(self) -> int:
        if not self.s1:
            return None
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# solution 2
'''
Push in O(1)
and pop and top in O(N)
'''
class MyQueue:

    def __init__(self):
        self.s1 = []        
        self.s2 = []        

    def push(self, x: int) -> None:
        while len(self.s1):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while len(self.s2):
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        if not self.s1:
            return None
        return self.s1.pop()

    def peek(self) -> int:
        if not self.s1:
            return None
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# solution 3
class MyQueue:

    def __init__(self):
        self.s1 = []        
        self.s2 = []        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()