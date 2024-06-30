# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute Force: Hashing
        # TC: O(N)
        # SC: O(N)

        # if head == None or head.next == None:
        #     return None

        # hashMap = defaultdict(ListNode)
        # temp = head
        # pos = 0 # 0-indexed(given)

        # while temp != None:
        #     if temp in hashMap:
        #         return temp

        #     hashMap[temp] = pos
        #     pos += 1
        #     temp = temp.next

        # return None

        # d = distance from node cycle begins to fast == slow
        # l1 = distance from the start of the LL to the first node of cycle
        # Length of the loop = d + l1

        # Optimal: Slow and Fast Pointer
        # TC: O(N)
        # SC: O(1)

        if head == None or head.next == None:
            return None

        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None


        


        