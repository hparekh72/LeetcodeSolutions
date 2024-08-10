# TC: O(n * m) + O(4 * n * m) ~ O(n * m)
# SC: O(n * m) (queue in bfs) + O(n * m) (distance) + O(n * m) (visited) ~ O(n * m)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        distance = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append([[r, c], 0])
                    visited[r][c] = 1
        
        # Up, Down, Left, Right
        dRow = [-1, 1, 0, 0]
        dCol = [0, 0, -1, 1]
        # TC: O(4 * n * m)
        while queue:
            node = queue.popleft()
            position, dist = node[0], node[1]
            r, c = position[0], position[1]
            distance[r][c] = dist

            for i in range(4):
                row = r + dRow[i]
                col = c + dCol[i]

                if row >= 0 and row < rows and col >= 0 and col < cols and visited[row][col] != 1:
                    queue.append([[row, col], dist + 1])
                    visited[row][col] = 1

        return distance

            

        
                    
        