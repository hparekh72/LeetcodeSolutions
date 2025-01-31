class Solution:

    # Brute Force:
    # 1) Recursively generate all possible combinations of 2 * n parentheses.
    # 2) Filter out only the valid ones.
    # TC: O(2^2n) * n
    # SC: O(2^n)

    def generateParenthesis(self, n: int) -> List[str]: # Backtracing (Optimal)
        # only add open parenthesis if open < n
        # only add a closing parenthesis if open > close
        # Stop when Open == Close == n

        res = []
        stack = []

        def backtrack(openCount, closeCount):
            # Base Condition
            if openCount == closeCount == n:
                res.append("".join(stack))

            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop() # backtrack

            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()    # backtrack

        backtrack(0, 0)
        return res  
        