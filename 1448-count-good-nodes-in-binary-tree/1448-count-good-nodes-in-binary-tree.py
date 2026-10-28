# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root :
            return 0

        def dfs(root,maxx):
            if not root :
                return 0
            good = 0
            if root.val >= maxx:
                maxx = root.val
                good = 1 

            return good + dfs(root.right,maxx) + dfs(root.left,maxx)        
        
        return dfs(root,root.val)


