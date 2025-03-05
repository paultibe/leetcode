# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse linked list, reversing each node, then return prev
        if not head:
            return head
        stack = [head]
        prev = None
        while stack:
            curr = stack.pop()
            temp = curr.next
            curr.next = prev
            if temp:
                stack.append(temp)
            prev = curr
        return prev