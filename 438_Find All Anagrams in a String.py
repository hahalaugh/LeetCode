import collections


class Solution(object):

    def findAnagrams(self, s, p):
        if not p or not s: return []
        
        result = []
        d = collections.Counter(p)
        counter = len(d)
        i, j = 0, 0
        
        # print(s.findAnagrams("cbaebabacd", "abc"))
        while j < len(s):
            if counter > 0:
                if s[j] in d:
                    d[s[j]] -= 1
                    if d[s[j]] == 0: 
                        counter -= 1
                j += 1

            while counter == 0:
                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] > 0:
                        if j - i == len(p):
                            result.append(i)
                        counter += 1
                i += 1
    
        return result
        
    def findAnagramsMN(self, s, p):
        # LTE
        if not p or not s: return []
        
        def isAnagram(s, p):
            if not p and not s: return True
            if (not p or not s) or (len(s) != len(p)):
                return False
            
            d = collections.defaultdict(int)
            for i in range(len(s)):
                d[s[i]] += 1
                d[p[i]] -= 1
            
            return len([_ for _ in d.values() if _ != 0]) == 0
        
        result = []
        for i in range(len(s) - len(p) + 1):
            if isAnagram(s[i:i + len(p)], p):
                result.append(i)
        return result
        
    def findAnagramsBacktrackingPermutation(self, s, pattern):
        # LTE
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        def getAnagrams(s):
            result = set()
            
            def bc(r, s):
                if not s:
                    result.add(r)
                else:
                    for i in range(len(s)):
                        r += s[i]
                        temp = s.pop(i)
                        bc(r, s)
                        s.insert(i, temp)
                        r = r[:-1]

            bc('', s)
            return result

        result = []
        anas = getAnagrams(list(pattern))
        print(anas)
        for i in range(len(s) - len(pattern)):
            if s[i:i + len(pattern)] in anas:
                result.append(i)
                
        return result


s = Solution()
#print(s.findAnagrams("cbaebabacd", "abc"))
#print(s.findAnagrams("abab", "ab"))
#print(s.findAnagrams("baa", "aa"))
print(s.findAnagrams("abaacbabc", "abc"))
