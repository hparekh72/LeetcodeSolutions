"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': # Brute Force
    #     # TC: O(2N) ~ O(N)
    #     # SC: O(N)

    #     oldToCopy = {None: None} # Edge case to handle temp.random == None

    #     temp = head
    #     while temp:
    #         copy = Node(temp.val)
    #         oldToCopy[temp] = copy
    #         temp = temp.next
        
    #     temp = head
    #     while temp:
    #         copy = oldToCopy[temp]
    #         copy.next = oldToCopy[temp.next]
    #         copy.random = oldToCopy[temp.random]
    #         temp = temp.next

    #     return  oldToCopy[head]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': # Space Optimization (Optimal)
        # TC: O(3N) ~ O(N)
        # O(1)

        # Step1: Insert copy nodes in between
        # Step2: Connect Random Pointers
        # Step3: Get Deep Copy List 

        self.insertCopyNodesInBetween(head)
        self.connectRandomPointers(head)
        return self.getDeepCopyList(head)

    def insertCopyNodesInBetween(self, head):
        temp = head

        while temp:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = copyNode.next # Moving to the next original node

    def connectRandomPointers(self, head):
        temp = head
        while temp:
            copyNode = temp.next
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None

            temp = temp.next.next # Moving to the next original node

    def getDeepCopyList(self, head):
        temp = head
        dummyNode = Node(-1)
        res = dummyNode

        while temp:
            copyNode = temp.next
            
            res.next = copyNode
            res = res.next # Move res to next node

            # Disconnecting and going back to the initial state of the LL
            temp.next = temp.next.next
            temp = temp.next # Move temp to next node

        return dummyNode.next


        
    




