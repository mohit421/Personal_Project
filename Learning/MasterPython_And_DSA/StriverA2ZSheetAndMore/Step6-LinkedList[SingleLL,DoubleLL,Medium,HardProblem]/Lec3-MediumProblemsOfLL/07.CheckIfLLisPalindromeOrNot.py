'''

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = deque()
        temp = head
        while temp is not None:
            st.append(temp.val)
            temp = temp.next
            
        temp = head
        while temp is not None:
            if temp.val != st.pop():
                return False
            temp = temp.next
        return True
