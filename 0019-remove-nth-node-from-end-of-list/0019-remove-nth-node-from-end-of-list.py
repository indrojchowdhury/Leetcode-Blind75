# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both
        while fast.next:
            slow = slow.next
            fast = fast.next

        # delete node
        slow.next = slow.next.next

        return dummy.next
        