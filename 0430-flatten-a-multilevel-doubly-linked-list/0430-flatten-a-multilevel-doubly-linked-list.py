"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        stack = [head]
        prev = None # "tail" of currently flattened list
        
        while stack:
            curr = stack.pop()
            
            # add to end of the list we're building
            if prev:
                prev.next = curr
                curr.prev = prev
            
            if curr.next: 
                stack.append(curr.next)
            if curr.child: 
                stack.append(curr.child) # (child is popped first)
                curr.child = None
            
            prev = curr
            
        return head
        