# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root,hi,lo):
            if root is None:
                return True
            
            if lo<root.val<hi:
                return check(root.left,root.val,lo) and check(root.right,hi,root.val)
            else:
                return False
        return check(root,float('inf'),float('-inf'))