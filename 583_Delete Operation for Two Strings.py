class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return 0 if not word2 else len(word2)
        d = {}
        
        def dp(i, j):
            if (i,j) in d:
                return d[(i, j)]
            elif i == -1 or j == -1:
                d[(i, j)] = j + 1 if i == -1 else i + 1
            elif word1[i] == word2[j]:
                d[(i, j)] = dp(i-1, j-1)
            else:
                d[(i, j)] = min(dp(i-1, j), dp(i, j-1))+1
            return d[(i, j)]
        
        return dp(len(word1)-1, len(word2)-1)
    