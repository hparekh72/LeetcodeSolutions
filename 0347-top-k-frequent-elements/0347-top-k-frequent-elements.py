import heapq
from collections import Counter

# TC: O(nlogk)
# SC: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        # Use heap 
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        # Extract the top k element from the heap
        top_k = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            top_k.append(num)

        return top_k

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     top_k = dict(heapq.nlargest(k, count.items(), key=lambda item: item[1])).keys()
    #     return top_k

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     return dict(Counter(nums).most_common(k)).keys()

            

