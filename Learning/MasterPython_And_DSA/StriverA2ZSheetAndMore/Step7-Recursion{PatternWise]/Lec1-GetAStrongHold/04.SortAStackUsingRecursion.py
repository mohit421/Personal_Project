'''

'''


# Solution
'''
🔹 Time Complexity

We have two recursive functions:

Sorted(s)

Pops one element, recursively sorts the remaining stack of size n-1, then calls insert_s to place the element back.

This recursion depth is O(n) (where n = size of stack).

insert_s(s, temp)

In the worst case, it may pop every element until the right position is found.

Each call to insert_s takes O(n) in the worst case.

So for each element (n times), we may need to do O(n) work →



🔹 Space Complexity

The recursion stack (call stack) can go as deep as:

O(n) calls for Sorted

O(n) calls for insert_s in the worst case

But these are nested, not additive (since insert_s happens inside one Sorted frame).

So total auxiliary space used = O(n) (recursion stack).

The stack s itself is the input, not extra space.

✅ Final Answer

Time Complexity:  O(N^2)

Space Complexity: O(n)
O(n) (due to recursion)
'''
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    
    
    def insert_s(self, s, temp):
        if not s or temp > s[-1]:   # put larger elements closer to top
            s.append(temp)
            return
        top = s.pop()
        self.insert_s(s, temp)
        s.append(top)

    def Sorted(self, s):
        if s:
            temp = s.pop()
            self.Sorted(s)
            self.insert_s(s, temp)