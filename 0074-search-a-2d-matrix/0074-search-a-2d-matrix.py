class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # Optimal
        # TC: O(logm + logn) = O(log mn)
        # SC: O(1)

        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // COLS
            col = mid % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False


        