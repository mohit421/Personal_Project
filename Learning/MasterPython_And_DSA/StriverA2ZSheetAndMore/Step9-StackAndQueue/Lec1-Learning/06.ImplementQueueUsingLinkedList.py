'''
All operatiion is O(1) using linkedlist 
TC is much much better using linkedlist
'''


        
        
# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.start = None
        self.end = None
        self.sz = 0

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.start is None
        

    def enqueue(self, x):
        # Add element x to the rear
        ele = Node(x)
        if self.start is None:     # empty queue
            self.start = ele
            self.end = ele
        else:
            self.end.next = ele
            self.end = ele
        self.sz += 1

        

    def dequeue(self):
        # Remove the front element
        if self.start is None:
            return -1
        else:
            self.start = self.start.next
            self.sz -= 1
            if self.start is None:
                self.end  = None


    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.start is None:
            return -1
        return self.start.data

    def size(self):
        # Return current size
        return self.sz
