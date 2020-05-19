class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = collections.Counter(t)
        counter = len(d)
        i, j = 0, 0
        result = s
        found = False
        
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
                        counter += 1
                        if j - i <= len(result):
                            found = True
                            result = "".join(s[i:j])
        
                i += 1
        
        return result if found else ""
    