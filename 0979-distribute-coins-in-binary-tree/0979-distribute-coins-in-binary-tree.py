# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return 0,0,0
            lcount, lcoin, ldis = solve(root.left) 
            rcount, rcoin, rdis = solve(root.right) 
            dis = ldis+rdis+lcount+rcount+lcoin+rcoin
            coin = lcoin+rcoin+ ((root.val - 1) if root.val else 0) 
            count = lcount+rcount+ (not root.val) 
            return max(0,count-coin),max(0,coin-count),dis
        return solve(root)[-1]
            