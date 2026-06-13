# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Lowest Common Ancestor in Binary Search Tree
# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l, h = p, q
        if l.val > h.val:
            l, h = h, l

        if l.val <= root.val <= h.val:
            return root
        elif root.val <= l.val:
            return self.lowestCommonAncestor(root.right, l, h)
        elif root.val >= h.val:
            return self.lowestCommonAncestor(root.left, l, h)
