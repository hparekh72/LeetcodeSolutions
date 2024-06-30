# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force: Hashing

        if head == None or head.next == None:
            return None

        hashMap = defaultdict(ListNode)
        temp = head
        pos = 0 # o-indexed(given)

        while temp != None:
            if temp in hashMap:
                return temp

            hashMap[temp] = pos
            pos += 1
            temp = temp.next

        return None


        