class TrieNode(object):

    def __init__(self, val=None):
        self.val = val
        self.next = {}
        self.isWord = False

        
class Trie(object):

    def __init__(self, d):
        self.root = TrieNode()
        self.cur = self.root
        for word in d:
            node = self.root
            for c in word:
                if c not in node.next:
                    node.next[c] = TrieNode(c)
                node = node.next[c]
            node.isWord = True

    def navi(self, c):
        if c in self.cur.next:
            self.cur = self.cur.next[c]
        else:
            self.cur = None
        return self.cur
    
    def reset(self, node=None):
        if node:
            self.cur = node
        else:
            self.cur = self.root
            

class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        t = Trie(wordDict)
        d = {}
        
        def dfs(idx):
            if idx == len(s): 
                return False
            
            if idx in d: 
                return d[idx]
            
            node = t.navi(s[idx])
            if not node:
                d[idx] = False
            elif idx == len(s) - 1:
                d[idx] = node.isWord
            else:
                if node.isWord:
                    t.reset()
                    if dfs(idx + 1):
                        d[idx] = True
                    else:
                        t.reset(node)
                        d[idx] = dfs(idx + 1)
                else:
                    d[idx] = dfs(idx + 1)
            return d[idx]
            
        return dfs(0)
    
    def wordBreakDP(self, s, wordDict):
        d = set(wordDict)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        i, j = 0, 1
        while j < len(s) + 1:
            temp = i
            while i >= 0:
                if not dp[i] or s[i:j] not in d: 
                    i -= 1
                else:
                    i = j
                    dp[j] = 1
                    break
            if dp[j] == 0:
                i = temp
            j += 1
        
        return dp[-1]


s = Solution()
print(s.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
