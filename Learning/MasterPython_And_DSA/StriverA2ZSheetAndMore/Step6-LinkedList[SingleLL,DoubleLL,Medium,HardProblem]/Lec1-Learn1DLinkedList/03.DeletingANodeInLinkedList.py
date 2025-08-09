'''

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node or not node.next:
            return
        node.val = node.next.val
        node.next = node.next.next




# GFG Code
'''
https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1
'''

# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    if x == 1:
        return head.next

    curr = head
    for i in range(x - 2):
        if curr is None or curr.next is None:
            return head  # index out of range
        curr = curr.next

    if curr.next:
        curr.next = curr.next.next

    return head