class Solution:
    # def isValid(self, s: str) -> bool: # Brute Force
    #     # TC: O(n^2)
    #     # SC: O(n)

    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace("()", "")
    #         s = s.replace("{}", "")
    #         s = s.replace("[]", "")
    #     return s == ""
    
    def isValid(self, s: str) -> bool: # Stack
        # TC: O(n)
        # SC: O(n)

        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False


    

        