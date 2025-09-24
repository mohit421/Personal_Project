'''
1. What is a Queue?

A queue is a linear data structure that follows FIFO (First In, First Out).

Example: A line at a ticket counter 🎟️. The first person to join is the first served.

2. Queue Operations

Enqueue → Add an element at the rear.

Dequeue → Remove an element from the front.

Front / Peek → Get the front element without removing it.

Rear → Get the last element.

isEmpty → Check if the queue is empty.

Size → Number of elements in the queue.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return "Queue Underflow"

    def peekFront(self):
        if not self.isEmpty():
            return self.queue[0]
        return "Empty Queue"

    def peekRear(self):
        if not self.isEmpty():
            return self.queue[-1]
        return "Empty Queue"

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print(q.peekFront())  # 5
print(q.dequeue())    # 5
print(q.size())       # 2


| Operation | List | deque | queue.Queue |
| --------- | ---- | ----- | ----------- |
| Enqueue   | O(1) | O(1)  | O(1)        |
| Dequeue   | O(n) | O(1)  | O(1)        |
| Peek      | O(1) | O(1)  | O(1)        |
| isEmpty   | O(1) | O(1)  | O(1)        |
| Size      | O(1) | O(1)  | O(1)        |



from queue import Queue

q = Queue()

print(q.empty())   # True → empty

q.put(100)
print(q.empty())   # False → not empty

'''
'''

'''
class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.queue = []
        self.n = n
        
    def isEmpty(self):
        # Check if queue is empty
        return len(self.queue)==0
    
    def isFull(self):
        # Check if queue is full
        return len(self.queue) == self.n
    
    def enqueue(self, x):
        # Enqueue
        if self.isFull():
            return -1
        self.queue.append(x)

    
    def dequeue(self):
        # Dequeue
        if self.isEmpty():
            return -1
        return self.queue.pop(0)

    
    def getFront(self):
        # Get front element
        if self.isEmpty():
            return -1
        return self.queue[0]
       
    
    def getRear(self):
        # Get rear element
        if self.isEmpty():
            return -1
        return self.queue[-1]
        
        
        

# Striver version
'''
Time Complexity:

pop function: O(1)

push function: O(1)

top function: O(1)

size function: O(1)

Space Complexity:

Whole Queue: O(n)

'''
class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 16
        self.arr = [0] * self.maxSize


    def push(self, newElement: int) -> None:
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize
        self.arr[self.end] = newElement
        print("The element pushed is", newElement)
        self.currSize += 1


    def pop(self) -> int:
        if self.start == -1:
            print("Queue Empty\nExiting...")
        popped = self.arr[self.start]
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        self.currSize -= 1
        return popped


    def top(self) -> int:
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]


    def size(self) -> int:
        return self.currSize




if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())