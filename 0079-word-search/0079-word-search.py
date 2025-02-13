class Solution:

    # TC: O(n * m * 4^l(dfs)) 
    # Here, n * m are the board dimensions, l is the length of the word

    # SC: O(l) (recursive call stack) + O(l) (set)

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, ind):
            # Base Case
            if ind == len(word): # Word has found
                return True

            # If current position out of grid boundaries, or character does not match or already visited
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[ind] or (r, c) in path):
                return False

            # Character matches
            path.add((r, c)) # Mark the current position to the set as visited

            # Recursively explore all four directions
            res = (
                dfs(r+1, c, ind+1) or # Down
                dfs(r-1, c, ind+1) or # Up
                dfs(r, c-1, ind+1) or # Left
                dfs(r, c+1, ind+1) # Right
            )

            path.remove((r, c)) # Reset Path

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

