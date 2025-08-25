'''

'''


# Using Iterative Ways

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next =prev
            prev = curr
            curr = nxt
        return prev
    

# Using Recursive ways solution 1

'''
Complexity & gotchas

Time: O(n) — each node visited once.

Space: O(n) in Python because recursion uses the call stack.

Common bug: forgetting head.next = None creates a cycle (e.g., …→2→1↖).

'''


'''
reverse(1)
└─ reverse(2)
   └─ reverse(3)
      └─ reverse(4)
         └─ base → return 4
      # head=3:
      # 3.next.next=3; 3.next=None → return 4 (list: 4→3)
   # head=2:
   # 2.next.next=2; 2.next=None → return 4 (list: 4→3→2)
# head=1:
# 1.next.next=1; 1.next=None → return 4 (list: 4→3→2→1)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
    