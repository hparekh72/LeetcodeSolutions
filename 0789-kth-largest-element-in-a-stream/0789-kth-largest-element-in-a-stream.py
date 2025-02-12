# Brute Force: Sort the array 
# TC: __init__(): O(nlogn)
# TC: add(): O(n) (To add an element at a specific position in an sorted array)
# SC: O(n)

# Optimal: Min Heap 
# TC: __init__(): O(nlogk)
# TC: add(): O(logk) (To push and pop an element in the heap)
# SC: O(k)



class KthLargest:

    def __init__(self, k: int, nums: List[int]): # O(nlogk)
        self.k = k
        self.minHeap = []
        
        for num in nums:
            heapq.heappush(self.minHeap, num) 

            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

        return None
        
    def add(self, val: int) -> int: 
        heapq.heappush(self.minHeap, val) # O(logk)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # O(logk)

        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)