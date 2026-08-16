# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,range_val):

            if root is None:
                return True
                
            check_res =root.val>range_val[0] and root.val<range_val[1]

            if not check_res:
                return False

            left = helper(root.left,(range_val[0],root.val))

            right = helper(root.right,(root.val,range_val[1]))

            return check_res and left and right

        return helper(root,(float("-inf"),float("inf")))
            
            