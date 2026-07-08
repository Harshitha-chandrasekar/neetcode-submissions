class DLLNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = DLLNode(-1,-1)
        self.tail = DLLNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size+=1

    def remove_node(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size-=1

    def remove_tail(self):
        if self.size == 0:
            return None

        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_f = 0
        self.key_node_map = {}
        self.freq_list_map = collections.defaultdict(DoubleLinkedList)

    def update_freq(self,node):
        currf = node.freq
        self.freq_list_map[currf].remove_node(node)

        if self.min_f == currf and self.freq_list_map[currf].size == 0:
            self.min_f+=1

        node.freq+=1
        self.freq_list_map[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1

        node = self.key_node_map[key]
        self.update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.val = value
            self.update_freq(node)
            return

        if len(self.key_node_map) == self.capacity:
            lru_list = self.freq_list_map[self.min_f]
            node_to_evict = lru_list.remove_tail()
            self.key_node_map.pop(node_to_evict.key)

        new_node = DLLNode(key,value)
        self.key_node_map[key] = new_node

        self.min_f = 1
        self.freq_list_map[1].add_node(new_node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)