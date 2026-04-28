class TimeMap:
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((timestamp,value))
        else:
            self.dict[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        arr=self.dict[key]
        ts = [t for t,v in arr]
        values = [v for t,v in arr]
        ans = -1
        left = 0
        right = len(ts) - 1
        while left <= right:
            middle = (left + right) // 2
            if ts[middle] <= timestamp:
                ans = middle
                left = middle + 1
            else:
                right = middle - 1
        return "" if ans == -1 else values[ans]
        
