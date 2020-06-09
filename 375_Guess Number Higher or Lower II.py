class Solution(object):

    def getMoneyAmount(self, n):
        if n == 1: return 0
        dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

        def solve(i, j):
            if i >= j: return 0
            if dp[i][j] != float('inf'): return dp[i][j]
            
            for x in range(i, j + 1):
                dp[i][j] = min(dp[i][j], x + max(solve(i, x - 1), solve(x + 1, j)))
            
            return dp[i][j]

        solve(1, n)
        return dp[1][n]