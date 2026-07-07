class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1]*k
        self.head = 0
        self.tail = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail%self.k] = value
        self.tail+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.head%self.k] = -1
        self.head+=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head%self.k]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail-1)%self.k]        

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return self.tail - self.head == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()