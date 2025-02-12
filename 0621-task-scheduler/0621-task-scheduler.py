class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Each tasks takes 1 unit time
        # Goal: minimize the idle time

        # TC: O(m * n) m-> len(tasks), n -> cooling time 
        # SC: O(m) 

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()] # MaxHeap
        heapq.heapify(maxHeap) # TC: O(m)

        time = 0
        queue = deque() # pairs of [-cnt, idleTime]

        while maxHeap or queue:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap) # 1 + heappop, since negative values due to Max Heap implementation
                if count < 0:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time




         