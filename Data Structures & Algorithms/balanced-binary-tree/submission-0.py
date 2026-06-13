# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
            if not node: return 0
            return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        if abs(leftheight - rightheight) > 1: return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
             
        