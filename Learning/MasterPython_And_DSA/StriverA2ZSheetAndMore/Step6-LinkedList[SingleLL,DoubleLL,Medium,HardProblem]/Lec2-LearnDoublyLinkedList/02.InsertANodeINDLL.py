'''
Problem:- 

✅ Final Time Complexity
Best Case: O(1) (if p = 0)

Worst Case: O(n) (if p is at the end)

➤ Overall Time Complexity: O(p), where p is the index after which the node is inserted.
⏱️ Space Complexity
You’re only creating one new node, and no other significant space is used.

➤ Space Complexity: O(1)

'''

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def addNode(self, head, p, x):
        # Code here
        curr = head
        node = Node(x)
        cnt = 0
        while curr:
            if cnt == p:
                if curr.next:
                    node.next = curr.next
                    curr.next.prev = node
                curr.next = node
                node.prev = curr
                return head
            cnt += 1
            curr = curr.next
            

# Other ways 

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def addNode(self, head, p, x):
        # Code here
        temp = head
        for i in range(0,p):
            if temp is None:
                return head
            temp = temp.next
        new_node = Node(x)
        if temp.next == None:
            temp.next = new_node
            new_node.prev = temp
        
        else:
            temp.next.prev = new_node
            new_node.next = temp.next
            temp.next = new_node
            new_node.prev = temp
        return head
            