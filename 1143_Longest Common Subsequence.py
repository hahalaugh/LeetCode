class Solution(object):

    def longestCommonSubsequence(self, text1, text2):
        # Top-Down ¹ý²»ÁË
        d = {}
        
        def topDown(i, j):
            if (i, j) in d:
                return d[(i, j)]
            
            result = 0
            
            if i < 0 or j < 0:
                return 0

            elif i == j == 0:
                result = 1 if text1[0] == text2[0] else 0

            elif text1[i] == text2[j]:
                result = topDown(i - 1, j - 1) + 1
                
            else:
                result = max(topDown(i, j - 1), topDown(i - 1, j))
            
            d[(i, j)] = result
            return d[(i, j)]

        return topDown(len(text1) - 1, len(text2) - 1)

    def longestCommonSubsequenceBottomTop(self, text1, text2):
        # Bottom-Top
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
                    
        return dp[-1][-1]
