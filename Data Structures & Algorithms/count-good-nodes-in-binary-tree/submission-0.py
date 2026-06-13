# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Count Good Nodes in Binary Tree
# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x
# Given the root of a binary tree root, return the number of good nodes within the tree.
# **** good, counter intuitive, understand why recursion - as we need to maintain a path and max so far!!
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(node, maxsofar) -> int:
            if node is None:
                return 0

            # is this node good?
            res = 1 if node.val >= maxsofar else 0
            if node.left:
                res += count_good_nodes(node.left, max(maxsofar, node.left.val))
            if node.right:
                res += count_good_nodes(node.right, max(maxsofar, node.right.val))

            return res

        return count_good_nodes(root, root.val)
