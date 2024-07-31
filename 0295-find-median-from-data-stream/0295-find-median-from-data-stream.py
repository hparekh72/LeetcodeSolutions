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


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()