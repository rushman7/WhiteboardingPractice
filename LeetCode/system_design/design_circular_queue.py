class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            node = Node(value)
            if self.isEmpty():
                self.head = self.tail = node
            else:
                self.tail.next = node
                self.tail = node
                
            self.size+=1
            return True
        
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            self.size -= 1
            return True
        
        return False

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity