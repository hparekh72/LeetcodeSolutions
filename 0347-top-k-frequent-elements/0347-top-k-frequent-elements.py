import heapq
from collections import Counter

# TC: O(nlogk)
# SC: O(n) + O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (val, key)) # Min-heap, since we need k most frequent elements
        
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for val, key in heap:
            res.append(key)

        return res



    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     top_k = dict(heapq.nlargest(k, count.items(), key=lambda item: item[1])).keys()
    #     return top_k

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     return dict(Counter(nums).most_common(k)).keys()

            

