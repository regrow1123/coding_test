# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        result = 0
        
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.val == node.left.val:
                left_arrow = left_length + 1
            if node.right and node.val == node.right.val:
                right_arrow = right_length + 1
                
            result = max(result, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
            
        dfs(root)
        return result