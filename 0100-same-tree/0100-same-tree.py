# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def tree(p,q):
            if not p and not q :
                return True
            if p and q :
                # print(p.val,q.val)
                if p.val != q.val :
                    return False
                return tree(p.left,q.left) and tree(p.right,q.right)
            else :
                return False
        return tree(p,q)