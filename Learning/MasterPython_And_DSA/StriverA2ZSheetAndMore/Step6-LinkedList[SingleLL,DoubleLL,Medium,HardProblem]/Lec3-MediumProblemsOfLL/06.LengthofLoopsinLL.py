'''

'''


# Brute force
'''
Time Complexity: O(N) The code traverses the entire linked list at least once, where 'N' is the number of nodes in the list. Therefore, the time complexity is linear, O(N).

Space Complexity: O(N) The code uses a hashmap/dictionary to store encountered nodes, which can take up to O(N) additional space, where ‘N' is the number of nodes in the list. Hence, the space complexity is O(N) due to the use of the map to track nodes.
'''

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        visited_node = {}
        temp = head
        timer = 0
        while temp is not None:
            if temp in visited_node:
                loop_len = timer - visited_node[temp]
                return loop_len
            visited_node[temp] = timer
            temp = temp.next
            timer += 1
        return 0
    



# Optimised solution

'''
Complexity Analysis

Time Complexity: O(N) The code traverses the entire linked list once, where 'n' is the number of nodes in the list. This traversal has a linear time complexity, O(n).

Space Complexity: O(1) The code uses only a constant amount of additional space, regardless of the linked list's length. This is achieved by using two pointers (slow and fast) to detect the loop without any significant extra memory usage, resulting in constant space complexity, O(1).
'''
'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        cnt = 1
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cnt = 1
                fast = fast.next
                while slow != fast:
                    cnt += 1
                    fast = fast.next
                return cnt
        return 0
        