class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Brute Force: Sorting
        # TC: O(n * nlogn)

        # Optimal: Max-Heap
        # TC: O(nlogn)
        # SC: O(k)

        maxHeap = [-stone for stone in stones] # Negate stones to simulate a max heap

        # Using heapify for efficient O(n) heap construction
        heapq.heapify(maxHeap)  # Now it behaves like a max heap due to negation

        while len(maxHeap) > 1: # TC: O(nlogn)
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -(y - x))

        maxHeap.append(0) # To handle Edge Case: stones = [2,2]
        return -maxHeap[0]




        