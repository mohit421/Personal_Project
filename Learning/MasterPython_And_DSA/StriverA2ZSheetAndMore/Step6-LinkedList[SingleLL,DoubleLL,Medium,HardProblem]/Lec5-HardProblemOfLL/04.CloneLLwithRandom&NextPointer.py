'''

'''

# Brute force using hashing (hashmap)

'''
Complexity Analysis

Time Complexity: O(2N) where N is the number of nodes in the linked list. The linked list is traversed twice, once for creating copies of each node and for the second time to set the next and random pointers for each copied node. The time to access the nodes in the map is O(1) due to hashing.

Space Complexity : O(N)+O(N)where N is the number of nodes in the linked list as all nodes are stored in the map to maintain mappings and the copied linked lists takes O(N) space as well.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dt = {}
        temp = head
        while temp:
            newNode = Node(temp.val)
            dt[temp] = newNode
            temp = temp.next
        
        temp = head
        while temp:
            clone = dt[temp]
            clone.next = dt.get(temp.next)
            clone.random = dt.get(temp.random)
            temp = temp.next
        
        return dt[head]
    


# ===============================
# Optimal Solution

'''
Complexity Analysis

Time Complexity: O(3N)where N is the number of nodes in the linked list. The algorithm makes three traversals of the linked list, once to create copies and insert them between original nodes, then to set the random pointers of the copied nodes to their appropriate copied nodes and then to separate the copied and original nodes.

Space Complexity : O(N) where N is the number of nodes in the linked list as the only extra additional space allocated it to create the copied list without creating any other additional data structures.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # copying each and every node in between
        if not head:
            return None
        temp = head
        while temp:
            nextEle = temp.next
            cloneNode = Node(temp.val)
            cloneNode.next = nextEle
            temp.next = cloneNode
            temp = nextEle
        
        # connect random pointer
        temp = head
        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
        
        # making sure that next pointer are connected
        temp = head
        dummyNode = Node(-1)
        res = dummyNode
        while temp:
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next

        return dummyNode.next

