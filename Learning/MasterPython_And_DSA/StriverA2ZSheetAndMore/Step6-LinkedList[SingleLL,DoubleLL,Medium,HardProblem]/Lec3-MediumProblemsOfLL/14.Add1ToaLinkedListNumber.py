'''
Add 1 to a Linked List Number

'''


'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
'''
TC:O(3N)
SC:- O(1)
'''
class Solution:
    
    def reverse(self, head):
        prev = None
        current = head
        
        while current:
            next_node = current.next  # store the next node
            current.next = prev       # reverse the link
            prev = current            # move prev forward
            current = next_node       # move current forward
        
        return prev
    def addOne(self,head):
        #Returns new head of linked List.
        head = self.reverse(head)
        temp, carry = head, 1
        while temp:
            temp.data = temp.data + carry
            if temp.data < 10:
                carry = 0
                break
            else:
                temp.data = 0
                carry = 1
            temp = temp.next
        
        if carry == 1:
            newNode = Node(1)
            head = self.reverse(head)
            newNode.next = head
            return newNode
        
        head = self.reverse(head)
        return head
            

        

# Using recursion we can do in one traversal

'''

'''

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

'''
TC: O(N)
SC:- O(N):- recursive stacks space used
'''

class Solution:
    
    def helper(self, temp):
        if temp == None:
            return 1
        carry  = self.helper(temp.next)
        temp.data = temp.data + carry
        if temp.data < 10:
            return 0
        temp.data = 0
        return 1
        
        return prev
    def addOne(self,head):
        #Returns new head of linked List.
        carry = self.helper(head)
        if carry:
            newNode = Node(1)
            newNode.next = head
            return newNode
        return head
    

'''
Iterative vs  Recursive

Iterative:
Pros: No Space
COns: Temporary data & more time taken

Recursive:-
'''

