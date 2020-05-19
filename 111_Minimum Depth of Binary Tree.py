# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        #DFS
        if not root: return 0
        if not root.left and not root.right: return 1
        l = self.minDepth(root.left) or float('inf')
        r = self.minDepth(root.right) or float('inf')
        return 1 + min(l, r)
    
    def minDepthBFS(self, root):
        #BFS
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        cur = 1
        q = [root]
        
        while q:
            step = len(q)
            for i in range(step):
                node = q.pop(0)
                if not node.left and not node.right:
                    return cur
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
            cur += 1
        
        