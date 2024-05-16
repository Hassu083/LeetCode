# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return True if root.val else False
        left = self.evaluateTree(root.left) 
        if not left and root.val == 3:
            return False
        if left and root.val == 2:
            return True
        right = self.evaluateTree(root.right) 
        return  left and right if root.val == 3 else left or right