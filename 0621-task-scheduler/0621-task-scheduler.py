class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Each tasks takes 1 unit time
        # Goal: minimize the idle time

        # TC: O(m * n) m-> len(tasks), n -> cooling time 
        # SC: O(m) 

        countMap = Counter(tasks)
        maxHeap = [-num for num in countMap.values()] # MaxHeap
        heapq.heapify(maxHeap) # O(m)

        queue = deque() # pairs if [-num, idleTime]
        time = 0
        while maxHeap or queue:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap) # 1 + heappop, since negative values due to Max Heap implementation
                if count < 0:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])    

        return time





        



        