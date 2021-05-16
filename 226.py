# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def inv_child(node):
            if not node:
                return
            
            inv_child(node.left)
            inv_child(node.right)
            
            node.left, node.right = node.right, node.left
        
        inv_child(root)
        return root