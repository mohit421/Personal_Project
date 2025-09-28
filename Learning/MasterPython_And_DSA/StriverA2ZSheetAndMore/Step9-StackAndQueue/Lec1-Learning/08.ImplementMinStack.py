'''

'''
'''
Time Complexity: O(1)

Space Complexity: O(2N)


Time Complexity

push(val)

Just comparisons, arithmetic, and append() → O(1)

pop()

Just pop() and maybe arithmetic to restore old min → O(1)

top()

Just list indexing and maybe returning mini → O(1)

getMin()

Direct return of mini → O(1)

👉 All operations are constant time.

✅ Space Complexity

Stack (self.st)

Stores 1 integer for every push (either actual value or encoded).

For n pushes → O(n)

Extra variable (self.mini)

Just one integer → O(1)

👉 Overall space = O(n)
'''
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val,val))
        else:
            self.st.append((val,min(val,self.st[-1][1])))

    def pop(self) -> None:
        if self.st:
            return self.st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1][0]
        return None

    def getMin(self) -> int:
        if self.st:
            return self.st[-1][1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# SOlution 2
'''
Time Complexity

push(val)

Constant work (comparison + append).

O(1)

pop()

Constant work (pop + maybe decode previous min).

O(1)

top()

Constant work (peek last + maybe return mini).

O(1)

getMin()

Just return mini.

O(1)

✅ Every operation runs in constant time.

pace Complexity

Stack storage:

Stores only one integer per push (either the real value or an encoded one).

Uses O(n) for n pushed elements.

Extra variable:

self.mini (single integer).

O(1)

✅ Total = O(n) space.
'''

class MinStack:

    def __init__(self):
        self.st = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if not self.st:
            self.mini = val
            self.st.append(val)
        else:
            if val<self.mini:
                self.st.append(2*val - self.mini)
                self.mini = val
            else:
                self.st.append(val)

    def pop(self) -> None:
        if not self.st:
            return None
        ele = self.st.pop()
        if ele<self.mini:
            self.mini = 2*self.mini - ele



    def top(self) -> int:
        if not self.st:
            return -1
        ele = self.st[-1]
        if ele <self.mini:
            return self.mini
        return ele

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()