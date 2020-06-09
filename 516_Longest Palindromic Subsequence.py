class Solution(object):

    def longestPalindromeSubseq(self, s):
        if not s: return 0
        
        n = len(s)
        dp = [[0] * (n) for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][n - 1]
    
    def longestPalindromeSubseq1DTopDown(self, s):
        if not s: return 0
        n = len(s)
        dp = {}
        
        def cal(i, j):
            if i > j: 
                return 0
            
            if i == j:
                return 1
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == s[j]:
                dp[(i, j)] = cal(i + 1, j - 1) + 2
            else:
                dp[(i, j)] = max(cal(i + 1, j), cal(i, j - 1))
            
            return dp[(i, j)]
        
        return cal(0, n - 1)
                
    def longestPalindromeSubseqCompareReverse(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        sr = s[::-1]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == sr[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
    
                
