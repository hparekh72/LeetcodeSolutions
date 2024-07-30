class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Brute Force: Sorting
        # TC: O(n * nlogn)

        # Optimal: Max-Heap
        # TC: O(nlogn)
        # SC: O(k)

        heap = [-num for num in stones]  # Negate stones to simulate a max heap

        # Using heapify for efficient O(n) heap construction
        heapq.heapify(heap)  # Now it behaves like a max heap due to negation

        while len(heap) > 1: # TC: O(nlogn)
            y = heapq.heappop(heap)
            y = -y
            x = heapq.heappop(heap)
            x = -x

            if x != y:
                heapq.heappush(heap, -(y - x))
        
        heap.append(0) # To handle Edge Case: stones = [2,2]
        return -heap[0]
            
        