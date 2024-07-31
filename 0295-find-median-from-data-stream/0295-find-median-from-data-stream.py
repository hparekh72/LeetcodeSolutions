# Brute Force 1: Sort the array before finding the median
# TC: O(n * nlogn)
# addNum(): O(1)
# findMedian(): O(nlogn)

# Brute Force 2: Add the elements in the array in a sorted fashion
# TC: O(n * n)
# addNum(): O(n)
# findMedian(): O(1)

# Optimal: Using small (Max-heap) and large (Min-heap) 
# TC: O(n*logn)
# addNum(): O(logn)
# findMedian(): O(1)

# Brute Force 1 code
class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        size = len(self.nums)
        if size % 2 == 1:
            return self.nums[size // 2]
        else:
            middle = size // 2
            if middle == 0:
                return self.nums[middle]
            else:
                return (self.nums[middle - 1] + self.nums[middle]) / 2


# Optimal: Using Heaps
# Note:
# Every element in the Small Heap (Max-Heap) <= Every element in the Large Heap (Min-Heap)
# Length of Small Heap (Max-Heap) ~ Length of Large Heap (Min-Heap) (Maximum 1 length difference)

class MedianFinder:

    def __init__(self):
        self.small = [] # Max-Heap
        self.large = [] # Min-Heap
        

    def addNum(self, num: int) -> None: # TC: O(logn)
        heapq.heappush(self.small, -num) # Negated, since Max-Heap

        # Make sure that every num in small <= every num in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            # Remove value from small and add in large
            val = heapq.heappop(self.small) 
            val = -val
            heapq.heappush(self.large, val)

        # Uneven Size? 
        if len(self.small) > len(self.large) + 1:
            # Remove value from small and add in large
            val = heapq.heappop(self.small) 
            val = -val
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            # Remove value from large and add in small
            val = heapq.heappop(self.large) 
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float: # TC: O(1)
        if len(self.small) > len(self.large):
            return -self.small[0] # Negative, since Max-Heap implementation in Python
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()