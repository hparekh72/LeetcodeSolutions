# Brute Force: Run DFS from each empty room
# TC: O(m*n)^2
# SC: O(m*n)

# Optimal: Instead of starting traversal from any wall, run BFS from each gate at the same time 
# TC: O(m*n)
# Sc: O(m * n) (visited and queue)


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None: # BFS Traversal (Multi Source BFS)
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()

        def addRoom(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or rooms[r][c] == -1:
                return 
            visited.add((r, c))
            queue.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = dist

                addRoom(r + 1, c) # Down
                addRoom(r - 1, c) # Up
                addRoom(r, c + 1) # Right
                addRoom(r, c - 1) # Left

            dist += 1


        
        