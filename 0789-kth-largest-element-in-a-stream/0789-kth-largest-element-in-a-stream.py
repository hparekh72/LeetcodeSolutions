class KthLargest:

    # Brute Force: Sort the array 
    # TC: __init__(): O(nlogn)
    # TC: add(): O(n) (To add an element at a specific position in an sorted array)
    # SC: O(n)

    # Optimal: Min Heap 
    # TC: __init__(): O(nlogk)
    # TC: add(): O(logk) (To push and pop an element in the heap)
    # SC: O(k)

    def __init__(self, k: int, nums: List[int]): # O(nlogk)
        self.heap = []
        self.k = k

        for num in nums:
            heapq.heappush(self.heap, num) # Min Heap

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

        return None

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) # O(logk)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap) # O(logk)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

