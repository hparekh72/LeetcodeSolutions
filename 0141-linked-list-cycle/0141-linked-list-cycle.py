# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute Force
        # TC: O(N)
        # SC: O(N)

        temp = head
        hashSet = set()
        while temp != None:
            if temp in hashSet:
                return True
            hashSet.add(temp)
            temp = temp.next

        return False

        