from random import choice
class RandomizedSet:
    def __init__(self):
        self.set = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        
        self.set[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        
        deleted_index = self.set[val]
        
        self.set[self.list[-1]] = deleted_index
        
        self.list[deleted_index], self.list[-1] = self.list[-1], self.list[deleted_index]
        self.list.pop()
        
        del self.set[val]
        
        return True
        

    def getRandom(self) -> int:
        return choice(self.list)
