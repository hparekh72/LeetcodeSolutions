# class MinStack: # Brute Force 

#     def __init__(self): # TC: O(1)
#         self.stack = []
        
#     def push(self, val: int) -> None: # TC: O(1)
#         self.stack.append(val)
        

#     def pop(self) -> None: # TC: O(1)
#         self.stack.pop()
        

#     def top(self) -> int: # TC: O(1)
#         return self.stack[-1]
        

#     def getMin(self) -> int: # TC: O(n)
#         return min(self.stack)

class MinStack: # Two Stack (Optimal)
    # TC: O(1)
    # SC: O(n)

    def __init__(self): 
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None: # TC: O(1)
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:  
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None: # TC: O(1)
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int: # TC: O(1)
        return self.stack[-1]
        

    def getMin(self) -> int: # TC: O(1)
        return self.minStack[-1]

    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()