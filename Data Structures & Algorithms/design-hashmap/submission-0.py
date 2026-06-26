class MyHashMap:

    def __init__(self):
        self.maps = {}

    def put(self, key: int, value: int) -> None:
        self.maps[key] = value

    def get(self, key: int) -> int:
        if key in self.maps:
            return self.maps[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.maps:
            self.maps.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)