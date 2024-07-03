# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Recursive Approach
        # TC: O(N)
        # SC: (N) (Recursive Stack Space)

        # Check if we need to reverse the group
        temp = head
        for _ in range(k):
            if temp == None:
                return head
            temp = temp.next

        # Reverse the group
        prev = None
        temp = head

        for _ in range(k):
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode

        # After reverse, we know that `head` is the tail of the group.
        # And `temp` is the next pointer in original linked list order
        head.next = self.reverseKGroup(temp, k)
        return prev

# ----------------------------------xxxxxxxxxxxxxxxxxxxxxxxx--------------------------------

        # Iterative Approach
        # TC: O(2N)
        # SC: O(1)

    #     if head.next == None:
    #         return head

    #     temp = head
    #     prev = None
    #     while temp != None:      
    #         kthNode = self.findKthNode(temp, k)
    #         if kthNode == None: 
    #             if prev != None:  # If total number of nodes < k 
    #                 prev.next = temp # Merge remaining nodes
    #             break

    #         nextNode = kthNode.next
    #         kthNode.next = None
    #         self.reverse(temp) # Reverse

    #         if temp == head:
    #             head = kthNode
    #         else:
    #             prev.next = kthNode

    #         prev = temp
    #         temp = nextNode

    #     return head


    # def reverse(self, head):
    #     temp = head
    #     prev = None
    #     while temp != None:
    #         nextNode = temp.next
    #         temp.next = prev
    #         prev = temp
    #         temp = nextNode

    #     return
            
    # def findKthNode(self, temp, k):
    #     count = 1
    #     while temp != None and count < k:
    #         temp = temp.next
    #         count += 1

    #     return temp



    


        
    