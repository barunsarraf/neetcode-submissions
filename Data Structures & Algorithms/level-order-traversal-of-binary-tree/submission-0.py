# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        def helper(root,level):
            if root is None:
                return
            if level in res:
                res[level].append(root.val)
            else:
                res[level] = [root.val]

            helper(root.left,level+1)
            helper(root.right,level+1)

        helper(root,0)

        return list(res.values())