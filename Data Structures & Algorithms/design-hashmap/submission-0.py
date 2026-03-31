class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hashmap = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        bucket = self.hashmap[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = key % self.size
        bucket = self.hashmap[index]

        for k, v in bucket:
            if k == key:
                return v
        
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.hashmap[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return