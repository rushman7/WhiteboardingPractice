class Node:
    def __init__(self, key=None, val=None, freq=1):
        self.val = val
        self.key = key
        self.freq = freq
        self.next = None
        self.prev = None
        
class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 2
    
    def insert(self, node):
        self.size+=1
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove(self, node=None):
        self.size-=1
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = self.tail.prev
            node.prev.next = self.tail
            self.tail.prev = node.prev
        node.prev = None
        node.next = None
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.freq_cache = {}
        self.node_cache = {}
        self.min_freq = {}

    def get(self, key):
        if key not in self.node_cache:
            return -1
        
        return self.adjust_freq(key).val
    
    def put(self, key, value):
        if key in self.node_cache:
            self.adjust_freq(key, value)
        else:
            if self.size == self.capacity:
                if self.capacity == 0:
                    return
                del self.node_cache[self.freq_cache[self.min_freq].remove().key]
                self.size-=1
                
            node = Node(key, value, 1)
            self.min_freq = 1
            if self.min_freq not in self.freq_cache:
                self.freq_cache[self.min_freq] = DLL()
            self.freq_cache[self.min_freq].insert(node)
            self.node_cache[key] = node
            self.size+=1
    
    def adjust_freq(self, key, value=None):
        node = self.node_cache[key]
        node = self.freq_cache[node.freq].remove(node)
        if node.freq == self.min_freq and self.freq_cache[self.min_freq].size == 2:
            self.min_freq+=1
        node.freq+=1
        if value:
            node.val = value
        if node.freq not in self.freq_cache:
            self.freq_cache[node.freq] = DLL()
        self.freq_cache[node.freq].insert(node)
        self.node_cache[node.key] = node

        return node