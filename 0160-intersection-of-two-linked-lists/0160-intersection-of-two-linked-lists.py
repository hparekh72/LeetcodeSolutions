# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Brute Force
        # TC: O(N)
        # SC: O(1)

        if not headA or not headB:
            return None
        
        temp1 = headA
        temp2 = headB
        hashSet = set()

        # Iterate over both lists
        while temp1 != None or temp2 != None:
            if temp1 != None:
                if temp1 in hashSet:
                    return temp1
                hashSet.add(temp1)
                temp1 = temp1.next

            if temp2 != None:
                if temp2 in hashSet:
                    return temp2
                hashSet.add(temp2)
                temp2 = temp2.next

        return None  # If no intersection is found