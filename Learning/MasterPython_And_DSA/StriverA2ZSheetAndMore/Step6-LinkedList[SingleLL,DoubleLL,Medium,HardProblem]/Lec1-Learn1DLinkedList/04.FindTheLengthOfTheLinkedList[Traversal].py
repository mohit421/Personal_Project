'''
https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1
'''

'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        curr = head
        l = 0
        while curr.next != None:
            curr = curr.next
            l += 1
        return l+1