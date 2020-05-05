class Solution(object):
    #DFS遍历一个岛，BFS膨胀 （切勿从已知岛的每个点开始BFS膨胀求最短路径）
    def shortestBridge(self, matrix):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        visited = set()
        q = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def findOne():
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 1:
                        return (i, j)
        
        def dfsPaintIsland(i, j, visited):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 1 and (i, j) not in visited:
                matrix[i][j] = 2
                visited.add((i, j))
                dfsPaintIsland(i, j+1, visited)
                dfsPaintIsland(i, j-1, visited)
                dfsPaintIsland(i+1, j, visited)
                dfsPaintIsland(i-1, j, visited)
        
        def bfsExpand(i, j):
            expand = 0
            visited = set()
            q = [(i, j)]
            visited.add((i, j))
            while q:
                step = len(q)
                for _ in range(step):
                    (x, y) = q.pop(0)
                    for (r, c) in [(x+d[0], y+d[1]) for d in directions]:
                        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                            if matrix[r][c] == 1:
                                return expand
                            if matrix[r][c] == 0 and (r, c) not in visited:
                                q.append((r, c))
                                visited.add((r, c))
                expand += 1
            return float('inf')
        
        
        (i, j) = findOne()
        dfsPaintIsland(i, j, set())
        
        m = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 2:
                    m = min(bfsExpand(i, j), m)
        return m
    
s = Solution()
print(s.shortestBridge([[0,1],[1,0]]))