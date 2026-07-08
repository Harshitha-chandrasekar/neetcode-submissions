class DLLNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.head = DLLNode(-1,-1) 
        self.tail = DLLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            self.head.next.prev = node
            node.prev = self.head
            self.head.next = node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value

            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.next.prev = node
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            return
        if len(self.hashmap) == self.capacity:
            lru = self.tail.prev
            self.hashmap.pop(lru.key)

            lru.prev.next = self.tail
            self.tail.prev = lru.prev

        
        
        new_node = DLLNode(key, value)
        self.hashmap[key] = new_node
        new_node.next = self.head.next
        self.head.next.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node

        
