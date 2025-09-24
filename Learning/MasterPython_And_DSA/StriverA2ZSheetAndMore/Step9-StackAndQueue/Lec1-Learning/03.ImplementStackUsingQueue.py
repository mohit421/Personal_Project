'''

'''

# Approach1 


import queue
class MyStack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()


    def push(self, x: int) -> None:
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        
        self.q1, self.q2 = self.q2, self.q1


    def pop(self) -> int:
        if self.q1.empty():
            return None
        return self.q1.get()

    def top(self) -> int:
        if self.q1.empty():
            return None
        top_ele = self.q1.get()
        self.q2.put(top_ele)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1
        return top_ele

    def empty(self) -> bool:
        return self.q1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()




# Approach 2

import queue
class MyStack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()


    def push(self, x: int) -> None:
        self.q1.put(x)


    def pop(self) -> int:
        if self.q1.empty():
            return None
        while self.q1.qsize()>1:
            self.q2.put(self.q1.get())
        popped = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return popped

    def top(self) -> int:
        if self.q1.empty():
            return None
        while self.q1.qsize()>1:
            self.q2.put(self.q1.get())
        top_ele = self.q1.get()
        self.q2.put(top_ele)
        self.q1, self.q2 = self.q2, self.q1
        return top_ele


    def empty(self) -> bool:
        return self.q1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


'''
Summary:

Approach 1 → costly push() but cheap pop().

Approach 2 → cheap push() but costly pop().
'''