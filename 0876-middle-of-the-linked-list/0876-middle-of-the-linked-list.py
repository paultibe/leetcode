# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if fast at last element, return slow

        slow = ListNode(0, head)
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next