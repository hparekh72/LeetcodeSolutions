# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Iterative Approach
        # TC: O(n)
        # SC: O(1)

        if head.next == None:
            return head

        temp = head
        prev = None

        while temp:
            kthNode = self.findKthNode(temp, k)
            if kthNode == None:
                if prev:    # If total no. of nodes less than k
                    prev.next = temp    # Merge remaining nodes
                break

            nextNode = kthNode.next
            kthNode.next = None
            self.reverse(temp)

            if temp == head:    # For 1st time
                head = kthNode
            else:
                prev.next = kthNode

            prev = temp
            temp = nextNode

        return head

    def findKthNode(self, temp, k):
        count = 1
        while temp and count < k:
            count += 1
            temp = temp.next
        return temp

    def reverse(self, head):
        temp = head
        prev = None

        while temp:
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode

        return prev


        
        
        