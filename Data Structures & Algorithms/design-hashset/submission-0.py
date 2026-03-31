class MyHashSet:

    def __init__(self):
        #this is there to intialize an empty hashset of length 100001 this is a fixed size as this is the most number of ops to be 
        self.size = 1_000_001
        self.hash_set= [False] * self.size

    def add(self, key: int) -> None:
        self.hash_set[key]=True 
        

    def remove(self, key: int) -> None:
        self.hash_set[key]=False
        

    def contains(self, key: int) -> bool:
        return self.hash_set[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)