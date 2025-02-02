class TimeMap:
    # TC: set(): O(1), get(): O(logn)
    # SC: O(m * n) m-> no. of keys, n-> total no. of values associated with the key

    def __init__(self):
        self.store = {} # key: List of pairs of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str: # O(logn)
        res = ""
        values = self.store.get(key, [])

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)