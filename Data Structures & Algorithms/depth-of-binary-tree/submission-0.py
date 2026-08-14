# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root,level):
            if root is None:
                return level

            if not root.left and not root.right:
                return level+1

            return max(helper(root.left,level+1),helper(root.right,level+1))

        return helper(root,0)