"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        
        cur = [root]
        result = []
        
        while cur:
            r = []
            step = len(cur)
            for i in range(step):
                node = cur.pop(0)
                r.append(node.val)
                if node.children:
                    cur.extend(node.children)
            
            result.append(r)
        
        return result
            
