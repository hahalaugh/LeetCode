"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    #Solution 1. DFS遍历，注意用哈希表判断成环
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}
        
        def dfs(node):
            if not node: 
                return None
            
            if node.val in visited: 
                return visited[node.val]

            visited[node.val] = Node(node.val)
            if not node.neighbors: 
                return visited[node.val]
            
            cur = visited[node.val]
            for neighbor in node.neighbors:
                cur.neighbors.append(dfs(neighbor))

            return cur
        
        return dfs(node)
