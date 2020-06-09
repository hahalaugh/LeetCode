from __builtin__ import None


class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        # DFS
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = collections.defaultdict(list)
        for p in prerequisites:
            adj[p[0]].append(p[1])
        
        parent = {}
        
        def dfsVisit(v):
            for next in adj[v]:
                if next not in parent:
                    parent[next] = v
                    dfsVisit(next)

        for v in adj:
            if v not in parent:
                parent[v] = None
                dfsVisit(v) 
        return True
