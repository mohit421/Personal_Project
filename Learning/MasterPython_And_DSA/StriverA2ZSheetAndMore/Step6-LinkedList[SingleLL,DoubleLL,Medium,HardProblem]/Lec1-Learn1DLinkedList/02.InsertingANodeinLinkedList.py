'''
https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1


Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
'''

'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        if not head:
            return Node(x)
        else:
            curr = head
            while curr.next != None:
                curr = curr.next
            curr.next  = Node(x)
        return head