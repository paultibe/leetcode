# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # early exit, root can't be a cousin
        if root.val in [x, y]:
            return False
        
        # BFS
        queue = deque() # (node, parent)
        queue.append((root, None))
        nodesSeen = {} # val -> (depth, parent)
        currDepth = 0
        while queue:
            # process one level at a time
            for _ in range(len(queue)):
                # process
                curr, parent = queue.popleft()
                # add info about it
                nodesSeen[curr.val] = (currDepth, parent)
                # check if both nodes have been seen
                if x in nodesSeen and y in nodesSeen:
                    # check if same depth
                    if nodesSeen[x][0] != nodesSeen[y][0] or nodesSeen[x][1] == nodesSeen[y][1]:
                        return False
                    return True 
                if curr.left:
                    queue.append((curr.left, curr))
                if curr.right:
                    queue.append((curr.right, curr))
            # move to next level
            currDepth += 1

        