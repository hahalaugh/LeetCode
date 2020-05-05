class Solution(object):
    #���ַ���
    #1. ��1��ʼ��Brute Force + BFS
    #2. ��0��ʼ��Brute Force + BFS
    #3. DP. ��һ���ͷ��ʼ�����󣬵ڶ����β��ʼ������
    
    def updateMatrixOneBasedBFS(self, matrix):
        dist = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        q = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def bfs(i, j):
            q = [(i, j)]
            visited = set()
            visited.add((i, j))
            expand = 0
            while q:
                expand += 1
                step = len(q)
                for _ in range(step):
                    (x, y) = q.pop(0)
                    for (r, c) in [(x+d[0], y+d[1]) for d in directions]:
                        if 0 <= r < len(dist) and 0 <= c < len(dist[0]) and (r, c) not in visited:
                            if matrix[r][c] == 0:
                                return expand
                            else:
                                q.append((r, c))
                                visited.add((r, c))
            return expand
        
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dist[i][j] = bfs(i, j)
        
        return dist
    
    def updateMatrixBFSZeroBased(self, matrix):
    #Brute Force ��0��ʼ����0��ʼ���ӡ������Χ�ڵ�ľ�������Լ��ľ���+1��������Ǹ��ڵ㣬�����Ǹ��ڵ�ȥ����Ӱ�������ڵ�.BFS����������Ӱ�졣
        dist = []
        q = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for i in range(len(matrix)):
            r = []
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: 
                    r.append(0)
                    q.append((i,j))
                else: 
                    r.append(float('inf'))
            dist.append(r)
        
        while q:
            (i,j) = q.pop(0)
            for (x, y) in [(i+d[0],j+d[1]) for d in directions]:
                if 0 <= x < len(dist) and 0 <= y < len(dist[0]):
                    if dist[x][y] > dist[i][j] + 1:
                        dist[x][y] = dist[i][j] + 1
                        q.append((x, y))
        
        return dist
            
    def updateMatrixDP(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        #DP. ��һ���ͷ��ʼ�����󣬵ڶ����β��ʼ������
        dist = []
        for row in matrix:
            r = []
            for n in row:
                if n == 0: r.append(0)
                else: r.append(float('inf')-10000)
            dist.append(r)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j]+1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1]+1)
        
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][j] != 0:
                    if i < len(matrix)-1:
                        dist[i][j] = min(dist[i][j], dist[i+1][j]+1)
                    if j < len(matrix[0])-1:
                        dist[i][j] = min(dist[i][j], dist[i][j+1]+1)
        return dist