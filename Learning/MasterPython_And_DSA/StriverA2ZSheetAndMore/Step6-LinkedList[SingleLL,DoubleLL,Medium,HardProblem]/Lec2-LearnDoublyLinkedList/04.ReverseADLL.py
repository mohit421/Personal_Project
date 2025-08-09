'''

'''

# Brute force using sTACK 

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        
        if head is None:
            return None
        
        stack = []
        curr = head
        
        while curr is not None:
            stack.append(curr)
            curr = curr.next
        
        new_head = stack.pop()
        curr = new_head
        curr.prev = None
        
        while stack:
            node = stack.pop()
            curr.next = node
            node.prev = curr
            curr = node
        
        curr.next = None
        return new_head

# Optimised one

'''
Complexity Analysis

Time Complexity : O(N) We only have to traverse the doubly linked list once, hence our time complexity is O(N).

Space Complexity : O(1), as the reversal is done in place.
'''
'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        
        if head is None:
            return None
        
        curr = head
        prev = None
        
        while curr is not None:
            curr.prev, curr.next = curr.next, curr.prev
            prev = curr
            curr = curr.prev
        
        return prev