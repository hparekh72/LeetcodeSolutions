class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: O(n) + O(nlogn) + O(k)
        # SC: O(n)

        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # TC: O(n) + O(nlogk) + O(k)
    #     # SC: O(n) + O(k)

    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)

    #     # Min Heap O(nlogk)
    #     heap = []
    #     for num in count.keys():
    #         heapq.heappush(heap, (count[num], num))

    #         if len(heap) > k:
    #             heapq.heappop(heap)

        
    #     res = []

    #     for num in heap:
    #         res.append(num[1])

    #     return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: O(n) + O(n)
        # SC: O(n)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

            

        


        


        



        

            

        