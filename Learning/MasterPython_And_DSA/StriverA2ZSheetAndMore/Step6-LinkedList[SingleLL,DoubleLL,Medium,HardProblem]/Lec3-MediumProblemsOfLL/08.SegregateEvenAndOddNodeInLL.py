'''

'''
# Brute force

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1: Collect odd and even nodes separately
        odd_nodes = []
        even_nodes = []
        
        idx = 1
        curr = head
        while curr:
            next_node = curr.next
            curr.next = None  # break links to avoid cycles
            if idx % 2 == 1:
                odd_nodes.append(curr)
            else:
                even_nodes.append(curr)
            curr = next_node
            idx += 1
        
        # Step 2: Reconnect nodes in odd list order, then even list order
        dummy = ListNode(0)
        tail = dummy
        
        for node in odd_nodes + even_nodes:
            tail.next = node
            tail = node
        
        return dummy.next



# Optimised approach

'''
Complexity
Time: O(n) — one pass through the list.

Space: O(1) — reuses nodes, only a few pointers.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = ListNode(0)
        odd_head = odd
        even = ListNode(0)
        even_head = even
        idx = 1
        curr = head
        while curr:
            if idx%2==0:
                even_head.next = curr
                even_head = even_head.next
            else:
                odd_head.next = curr
                odd_head = odd_head.next
            
            curr = curr.next
            idx += 1

        even_head.next = None
        odd_head.next  = even.next
        return odd.next
    

# More optimised without using dummy nodes
'''
TC:- O(N)
SC:- O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head
            