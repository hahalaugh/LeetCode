class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        walk = 0
        target = 2
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        q = [(0,0)]
        visited = set()
        visited.add((0,0))
        
        mx = float('-inf')
        for row in forest:
            for n in row:
                mx = max(mx, n)

        found = False
        while q:
            step = len(q)
            for _ in range(step):
                (i, j) = q.pop(0)
                if forest[i][j] == target:
                    target += 1
                    if target > mx:
                        return walk
                    q = [(i, j)]
                    visited = set()
                    found = True
                    break
                else:
                    found = False
                    for (x, y) in [(i+d[0], j+d[1]) for d in dirs]:
                        if 0 <= x < len(forest) and 0 <= y < len(forest[0]) and forest[x][y] != 0 and (x, y) not in visited:
                            q.append((x, y))
                            visited.add((x, y))
            if not found:
                walk += 1

        return -1
        
        
s = Solution()
print(s.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))