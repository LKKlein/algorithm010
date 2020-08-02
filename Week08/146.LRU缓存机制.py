from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.datas = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.datas:
            value = self.datas.get(key)
            self.datas.move_to_end(key)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.datas:
            if value == self.datas.get(key):
                self.datas.move_to_end(key)
                return
            else:
                del self.datas[key]
        
        self.datas[key] = value
        if len(self.datas) > self.capacity:
            self.datas.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
