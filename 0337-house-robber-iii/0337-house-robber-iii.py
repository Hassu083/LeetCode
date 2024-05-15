# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None) 
        def dp(root):
            if not root:
                return 0
            ans = root.val
            if left:=root.left:
                if left.left:
                    ans += dp(left.left) 
                if left.right:
                    ans += dp(left.right) 
            if right:=root.right:
                if right.left:
                    ans += dp(right.left) 
                if right.right:
                    ans += dp(right.right) 
            return max(ans, dp(root.left)+dp(root.right)) 
        
        return dp(root) 