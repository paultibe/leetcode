# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # scratch notes
        # preorder = [3, 9, 20, 15, 7]
        # first is root
        # inorder = [9,3,15,20,7]
        # in order means root is always sandwiched in the middle
        # whatever to the left of 3 is left subtree
        # whatever is to the right is right subtree
        
        # base case
        if not preorder or not inorder:
            return
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        lastLeftIndex = inorder.index(rootVal)
        
        # recurse left
        root.left = self.buildTree(preorder[1:lastLeftIndex + 1], inorder[:lastLeftIndex]) # + 1 because non inclusive
        # recurse right
        root.right = self.buildTree(preorder[lastLeftIndex + 1:], inorder[lastLeftIndex + 1:])

        return root