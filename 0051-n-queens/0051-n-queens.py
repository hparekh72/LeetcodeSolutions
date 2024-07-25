class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Brute:
        # TC: Exponential in nature since we are trying out all ways, to be precise its O(N! * N^2).
        # SC: O(N^2) + O(N) (recursive stack space) 
        
        # Optimal:
        # TC: Exponential in nature since we are trying out all ways, to be precise its O(N! * N).
        # SC: O(N^2) + O(N) (recursive stack space) + O(n) (set)

        # Optimal Approach

        # For tracking the columns which already have a queen
        cols = set()

        # This is required to identify diagonals, specifically for diagonals with increasing row and increasing col pattern
        negDiagonal = set() # r - c

        # This is required to identify antidiagonals, specifically for diagonals with increasing row and decreasing col pattern
        posDiagonal = set() # r + c
        
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            # Base Case
            if r == n:
                copy = ["".join(row) for row in board] # Deep copy
                res.append(copy)
                return 

            for c in range(n):
                # If the current square doesn't have another queen in same column and diagonal.
                if not (c in cols or (r + c) in posDiagonal or (r - c) in negDiagonal):
                    cols.add(c)
                    posDiagonal.add(r + c)
                    negDiagonal.add(r - c)
                    board[r][c] = 'Q' # place the queen

                    backtrack(r + 1)

                    # baktrack(reset the path)
                    cols.remove(c)
                    posDiagonal.remove(r + c)
                    negDiagonal.remove(r - c)
                    board[r][c] = '.' 

        backtrack(0) # row 0
        return res

                    







        