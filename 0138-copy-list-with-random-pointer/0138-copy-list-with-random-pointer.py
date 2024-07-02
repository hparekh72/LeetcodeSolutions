"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Optimal
        # TC: O(N)
        # SC: O(N)
        
        oldToCopy = {None: None}

        temp = head
        while temp != None:
            oldToCopy[temp] = Node(temp.val)
            temp = temp.next
            
        temp = head
        while temp != None:
            copy = oldToCopy[temp]
            copy.next = oldToCopy[temp.next]
            copy.random = oldToCopy[temp.random]

            temp = temp.next


        return oldToCopy[head]

        
        


