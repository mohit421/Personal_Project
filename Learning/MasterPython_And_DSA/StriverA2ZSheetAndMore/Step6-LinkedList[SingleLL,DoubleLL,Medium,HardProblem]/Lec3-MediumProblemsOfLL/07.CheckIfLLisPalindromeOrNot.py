'''

'''


# Brute force

'''
Time Complexity: O(2 * N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and compare with the linked list. Both traversals take O(2*N) ~ O(N) time.

Space Complexity: O(N) We use a stack to store the values of the linked list, and in the worst case, the stack will have all N values,  ie. storing the complete linked list.
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



# Optimised approach

'''

'''

