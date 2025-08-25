'''

'''

# Solution using Iterative ways

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            temp.val, temp.next.val = temp.next.val, temp.val
            temp = temp.next.next
        return head
    


# Using Recursive ways solution 1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head.val, head.next.val = head.next.val, head.val
        self.swapPairs(head.next.next)
        return head
    
# SOluyion2 recursive ways
'''
swapPairs([1,2,3,4])
│
├── swapPairs([3,4])
│   │
│   └── swapPairs([]) → None
│
└── returns [2 → 1 → 4 → 3]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first, second = head, head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second