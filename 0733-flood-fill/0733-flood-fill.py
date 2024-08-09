# BFS Implementation
# TC: O(4 * N * M) 
# SC: O(N * M) (queue)

# DFS Implementation
# TC: O(4 * N * M) 
# SC: O(N * M) (recursion stack space)


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # return self.bfs(image, sr, sc, color)
        startColor = image[sr][sc]
        self.dfs(image, sr, sc, color, startColor)
        return image

    def dfs(self, image, row, col, color, startColor):

        # Base Condition
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != startColor or image[row][col] == color:
            return 
        
        image[row][col] = color # Replace with new color

        self.dfs(image, row - 1, col, color, startColor) # Up
        self.dfs(image, row, col + 1, color, startColor) # Right
        self.dfs(image, row + 1, col, color, startColor) # Down
        self.dfs(image, row, col - 1, color, startColor) # Left


    def bfs(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])
        currentColor = image[sr][sc]

        queue = deque([(sr, sc)])
        image[sr][sc] = color


        # Up, Down, Left, Right
        dRow = [-1, 1, 0, 0] 
        dColumn = [0, 0, -1, 1]

        while queue:
            r, c = queue.popleft()

            for i in range(4):
                row = r + dRow[i]
                col = c + dColumn[i]

                if row < 0 or row >= rows or col < 0 or col >= cols or image[row][col] == color or image[row][col] != currentColor:
                    continue
                else:
                    queue.append([row, col])
                    image[row][col] = color # Replace with new color
        



    
        