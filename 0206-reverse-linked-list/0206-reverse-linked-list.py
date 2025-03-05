# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse linked list, reversing each node, then return prev
        
        def reverse(curr, prev):
            # base case, arrived at the end, nothign left to reverse
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev
            return reverse(temp, curr)
        
        return reverse(head, None)
        