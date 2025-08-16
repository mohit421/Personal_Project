'''

'''


# Solution 1

#User function Template for python3
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        temp = head
        while temp:
            if temp.data == key:
                if temp == head:
                    head = head.next
                nextNode = temp.next
                prevNode = temp.prev
                if nextNode:
                    nextNode.prev = prevNode
                if prevNode:
                    prevNode.next = nextNode
                temp = nextNode
            else:
                temp = temp.next
                
            
        return head
                
        

        