# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Kth Smallest Integer in BST
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

# A binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = deque([root])
        visited = set([root])

        # iterative in order -> sorted output at K
        while stack:
            top = stack[-1]
            if top.left and top.left not in visited:
                stack.append(top.left)
                visited.add(top.left)
                continue

            top = stack.pop()
            k -= 1
            if k == 0:  # 1-indexed and not 0 indexed
                return top.val

            if top and top.right and top.right not in visited:
                stack.append(top.right)
                visited.add(top.right)
                continue

        return -1
