class Node:
    def __init__(self, url: str):
        self.data = url
        self.prev = None
        self.next = None



class BrowserHistory:

    # TC: O(steps)
    # SC: O(N) N represents the number of nodes

    def __init__(self, homepage: str): # O(1)
        self.currentPage = Node(homepage) # Create a currentPage pointer to traverse
        

    def visit(self, url: str) -> None: # O(1)
        newNode = Node(url)
        newNode.prev = self.currentPage # Connect the new node (prev) with the previous node
        self.currentPage.next = newNode # Connect the previous (node) next with the new node
        self.currentPage = newNode      # Move to the newly created current page
        return None
        

    def back(self, steps: int) -> str: # O(steps)

        while steps > 0 and self.currentPage.prev != None:
            self.currentPage = self.currentPage.prev # Move one page/node behind
            steps -= 1
        
        return self.currentPage.data
        

    def forward(self, steps: int) -> str: # O(steps)

        while steps > 0 and self.currentPage.next != None:
            self.currentPage = self.currentPage.next # Move one page/node ahead
            steps -= 1
        
        return self.currentPage.data
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)