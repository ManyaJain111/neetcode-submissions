# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 and root2 :
                return False
            elif not root2 and root1:
                return False
            elif root1.val== root2.val:
                return sameTree(root1.left,root2.left) and sameTree(root1.right,root2.right)
            else:
                return False

        if not root:
            return False
        if not subRoot:
            return True
        if root.val== subRoot.val:
            if sameTree(root.left,subRoot.left) and  sameTree(root.right,subRoot.right):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        