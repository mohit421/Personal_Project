



# Brute force

'''
Complexity Analysis

Time Complexity: O(L)+O(L-N), We are calculating the length of the linked list and then iterating up to the (L-N)th node of the linked list, where L is the total length of the list.

Space Complexity:  O(1), as we have not used any extra space.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        cnt = 0
        temp = head
        while temp is not None:
            cnt += 1
            temp = temp.next
        if cnt == n:
            newHead = head.next
            head = None
            return newHead
        res = cnt - n
        temp = head

        while temp is not None:
            res -= 1
            if res == 0:
                break
            temp = temp.next
        delNode = temp.next
        temp.next = temp.next.next
        delNone = None
        return head





# Optimised APproach
'''
Complexity Analysis

Time Complexity: O(N) since the fast pointer will traverse the entire linked list, where N is the length of the linked list.

Space Complexity: O(1), as we have not used any extra space.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None  # or head, depending on your spec
        dummy = ListNode(0,head)
        fast = slow = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next