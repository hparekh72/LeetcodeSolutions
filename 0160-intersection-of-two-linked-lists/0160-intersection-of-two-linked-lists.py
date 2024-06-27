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

        # if head == None or headB == None:
        #     return None
        
        # temp1 = headA
        # temp2 = headB
        # hashSet = set()

        # # Iterate over both lists
        # while temp1 != None or temp2 != None:
        #     if temp1 != None:
        #         if temp1 in hashSet:
        #             return temp1
        #         hashSet.add(temp1)
        #         temp1 = temp1.next

        #     if temp2 != None:
        #         if temp2 in hashSet:
        #             return temp2
        #         hashSet.add(temp2)
        #         temp2 = temp2.next

        # return None  # If no intersection is found

        # Approach 2:
        # TC: O(2(N + M))
        # SC: O(1)

        temp1, temp2 = headA, headB
        length1, length2 = 0, 0

        while temp1 != None:
            length1 += 1
            temp1 = temp1.next

        while temp2 != None:
            length2 += 1
            temp2 = temp2.next

        temp1, temp2 = headA, headB

        if length1 > length2:
            diff = length1 - length2
            while diff > 0:
                temp1 = temp1.next
                diff -= 1

        elif length2 > length1:
            diff = length2 - length1
            while diff > 0:
                temp2 = temp2.next
                diff -= 1

        while temp1 != None:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        
        return None


