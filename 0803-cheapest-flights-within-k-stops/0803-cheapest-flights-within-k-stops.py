# Note: Here Dijkstra algorithm fails with Priority queue and distance array on this test case
# flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]

# Dijkstra's algorithm fails in scenarios like the Cheapest Flights Within K Stops problem because it it focuses solely on finding the shortest path based on the cumulative cost, regardless of how many stops are taken.

# Priority Queue Issue: Using a priority queue based solely on path costs can result in exploring cost-effective but too lengthy (in terms of stops) paths early on, potentially overlooking shorter (in stops) valid paths within the allowed number of stops.

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

#         # Create a adjacency list
#         graph = defaultdict(list)
#         for flight in flights:
#             graph[flight[0]].append([flight[1], flight[2]])

#         print(graph)

#         minHeap = []
#         heapq.heappush(minHeap, [0, src, 0]) # Price, city(node), stops

#         prices = [float('inf')] * n
#         prices[src] = 0

#         while minHeap:
#             price, city, stops = heapq.heappop(minHeap)
#             print(price, city, stops)

#             if city == dst:
#                 return price

#             if stops > k:
#                 continue

#             for neighborCity in graph[city]:
#                 newCity = neighborCity[0]
#                 newPrice = neighborCity[1]

#                 if price + newPrice < prices[newCity]:
#                     prices[newCity] = price + newPrice
#                     heapq.heappush(minHeap, [prices[newCity], newCity, stops + 1])
#                     print(minHeap)

#         return -1

# BFS Implementation
# TC: O(E) 
# SC: Memory Limit Exceeded

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

#         # Create a adjacency list
#         graph = defaultdict(list)
#         for flight in flights:
#             graph[flight[0]].append([flight[1], flight[2]])


#         queue = deque()
#         queue.append([0, src, 0]) # Price, city(node), stops

#         minPrice = float('inf')

#         # BFS Implementation
#         while queue:
#             price, city, stops = queue.popleft()

#             if city == dst:
#                 minPrice = min(price, minPrice)

#             if stops > k:
#                 continue

#             for neighborCity in graph[city]:
#                 newCity = neighborCity[0]
#                 newPrice = neighborCity[1]

#                 queue.append([price + newPrice, newCity, stops + 1])

#         # No route within K stops
#         if minPrice == float('inf'):
#             return -1
#         else:
#             return minPrice

# BFS Implementation
# TC: O(E) 
# SC: O(E) (adjacency list) + O(E) (queue)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Create a adjacency list
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append([flight[1], flight[2]])

        queue = deque()
        queue.append([0, src, 0]) # Stops, city(node), price

        prices = [float('inf')] * n
        prices[src] = 0

        # BFS Implementation
        while queue:        # TC: O(E) 
            stops, city, price = queue.popleft()

            if stops > k:
                continue

            for neighborCity in graph[city]:
                newCity = neighborCity[0]
                newPrice = neighborCity[1]

                if price + newPrice < prices[newCity] and stops <= k:
                    prices[newCity] = price + newPrice
                    queue.append([stops + 1, newCity, price + newPrice])

        # No route within K stops
        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]
        