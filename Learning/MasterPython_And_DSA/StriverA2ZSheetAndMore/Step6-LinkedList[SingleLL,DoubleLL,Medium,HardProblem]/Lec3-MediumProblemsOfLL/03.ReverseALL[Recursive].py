'''

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if temp == None or temp.next == None:
            return head
        rvr = self.reverseList(temp.next)
        temp.next.next = temp
        temp.next = None
        return rvr