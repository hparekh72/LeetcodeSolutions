# BFS Implementation
# TC: O(4 * N * M) 
# SC: O(N * M) (visited array) + O(N * M) (queue)


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        currentColor = image[sr][sc]
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque([(sr, sc)])
        image[sr][sc] = color
        visited[sr][sc] = 1


        # Up, Down, Left, Right
        dRow = [-1, 1, 0, 0] 
        dColumn = [0, 0, -1, 1]

        while queue:
            r, c = queue.popleft()

            for i in range(4):
                row = r + dRow[i]
                col = c + dColumn[i]

                if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] == 1 or image[row][col] != currentColor:
                    continue
                else:
                    queue.append([row, col])
                    image[row][col] = color
                    visited[row][col] = 1
        
        return image



    
        