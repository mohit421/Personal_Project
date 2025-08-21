'''

'''

# Brute Force Solution


# Optimised Solution
'''
TC:- O(N)
SC:- O(1)
'''

#Back-end complete function Template for Python 3

'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing lis
        prevNode = head
        while prevNode and prevNode.next:
            nextNode = prevNode.next
            while nextNode and nextNode.data == prevNode.data:
                nextNode = nextNode.next
            prevNode.next = nextNode
            if nextNode:
                nextNode.prev = prevNode
            prevNode = prevNode.next
        
        return head