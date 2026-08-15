# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(root,p1,p2):

            if root is None:
                return None

            if root.val == p1.val or p2.val == root.val:
                return root
            
            left = helper(root.left,p1,p2)
            right = helper(root.right,p1,p2)

            if left and right:
                return root
            
            if left:
                return left

            return right
        return helper(root,p,q)
