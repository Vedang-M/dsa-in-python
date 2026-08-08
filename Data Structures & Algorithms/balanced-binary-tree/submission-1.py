# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def max_depth(root):
            if root is None:
                return 0
            
            else:
                return 1+max(max_depth(root.left), max_depth(root.right))

        l = max_depth(root.left)
        r = max_depth(root.right)
        return(
            abs(l-r)<=1 
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )