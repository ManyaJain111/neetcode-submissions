# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def height(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     length= 1+ max(self.height(root.left),self.height(root.right))
    #     return length
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     self_dia= 0
    #     if not root:
    #         return 0
    #     else:
    #         dl= self.height(root.left)
    #         dr= self.height(root.right)
    #         self_dia= dl+dr
    #         left=self.diameterOfBinaryTree(root.left)
    #         right=self.diameterOfBinaryTree(root.right)
    #         self_dia= max(self_dia,left,right)
    #     return self_dia
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            self.dia= 0
            def height(root):
                if not root:
                    return 0
                
                dl= height(root.left)
                dr= height(root.right)
                new= dl+dr
                self.dia= max(self.dia,new)
                return 1 + max(dl,dr)
            height(root)
            return self.dia







        