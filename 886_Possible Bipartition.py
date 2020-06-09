class Solution(object):

    def possibleBipartition(self, n, dislikes):
        #BFS
        conn = collections.defaultdict(list)
        color = [0] * (n + 1)
        
        for d in dislikes:
            conn[d[0]].append(d[1])
            conn[d[1]].append(d[0])
        
        for idx in conn:
            if color[idx] != 0: continue
            c = 1
            color[idx] = 1
            q = [idx]
            while q:
                cur = q.pop(0)
                for next in conn[cur]:
                    if color[cur] == color[next]: return False
                    
                    if color[next] in [1, -1]:
                        continue
                    
                    color[next] = -color[cur]
                    q.append(next)
                    
        
        return True
    def possibleBipartitionDFS(self, n, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if not dislikes: 
            return True

        # 1 0 -1
        conn = collections.defaultdict(list)
        color = [0] * (n + 1)
        
        for d in dislikes:
            conn[d[0]].append(d[1])
            conn[d[1]].append(d[0])
        
        def paint(i, c):
            color[i] = c
            for next in conn[i]:
                if color[next] != 0 and color[next] != -c: return False
                if color[next] == 0 and not paint(next, -c): return False
            return True
        
        for i in conn:
            if color[i] == 0 and not paint(i, 1):
                return False
        
        return True