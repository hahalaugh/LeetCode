class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = {}

        def dp(i, j):
            if (i, j) in d:
                return d[(i, j)]
            elif i == -1 or j == -1:
                d[(i, j)] = i + 1 if j == -1 else j + 1 
            elif word1[i] == word2[j]:
                d[(i, j)] = dp(i - 1, j - 1)
            else:
                d[(i, j)] = min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1
            return d[(i, j)]
        
        return dp(len(word1) - 1, len(word2) - 1)


s = Solution()
print(s.minDistance("horse", "ros"))
