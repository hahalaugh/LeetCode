class TrieNode(object):

    def __init__(self, val):
        self.val = val
        self.next = {}
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode('')
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode(node.val + c)
            node = node.next[c]
        node.isWord = True

        
class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        t = Trie()
        result = []
        
        for word in words:
            t.insert(word)
        
        def dfs(node, i, j, firstHit):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != '#':
                # print(board)
                ch = board[i][j]
                board[i][j] = '#'
                r = []
                # print(ch, node.val, node.next.keys())
                if not node or ch not in node.next or ((i, j) == checking and not firstHit):
                    board[i][j] = ch 
                    return []
                node = node.next[ch]
                
                if node.isWord:
                    r.append(node.val)

                r.extend(dfs(node, i + 1, j, False))
                r.extend(dfs(node, i - 1, j, False))
                r.extend(dfs(node, i, j + 1, False))
                r.extend(dfs(node, i, j - 1, False))
                
                board[i][j] = ch 
                return r
            
            return []

        for i in range(len(board)):
            for j in range(len(board[0])):
                checking = (i, j)
                result.extend(dfs(t.root, i, j, True))
        return set(result)

s = Solution()
print(s.findWords([["a","a"]], ["a"]))