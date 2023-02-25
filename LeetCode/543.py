# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = float('-inf')
        def dfs(node):
            nonlocal diameter
            if node is None:
                return -1
            
            ld, rd = dfs(node.left), dfs(node.right)
            diameter = max(diameter, ld+rd+2)
            return max(ld, rd)+1
        dfs(root)
        return diameter