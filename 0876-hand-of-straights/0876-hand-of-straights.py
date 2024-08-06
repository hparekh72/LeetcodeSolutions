# Optimal: Using Greedy Approach
# TC: O(nlogn) + O(n)
# SC: O(n)

# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

#         if len(hand) % groupSize:
#             return False

#         hand.sort()
        
#         hashMap = defaultdict(int)

#         for i in range(len(hand)):
#             hashMap[hand[i]] += 1

#         while hashMap:

#             start = next(iter(hashMap))
#             for i in range(start, start + groupSize):

#                 if i not in hashMap:
#                     return False

#                 hashMap[i] -= 1
#                 if hashMap[i] == 0:
#                     del hashMap[i]

#         return True

# Optimal: Using Greedy Approach
# Similar approach as previous code, instead of sorting, we are using Min-Heap
# TC: O(nlogn) + O(n)
# SC: O(n)

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hashMap = {}
        for num in hand:
            hashMap[num] = 1 + hashMap.get(num, 0)

        minHeap = list(hashMap.keys())
        heapq.heapify(minHeap)

        while minHeap:

            start = minHeap[0]
            for i in range(start, start + groupSize):
                if i not in hashMap:
                    return False
                    
                hashMap[i] -= 1
                if hashMap[i] == 0:
                    # Only remove from heap if it's the current smallest element
                    # Ensures we don't pop out of order, which could miss a card
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True




        

        

          