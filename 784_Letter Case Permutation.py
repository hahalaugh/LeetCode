class Solution(object):

    def letterCasePermutation(self, letters):
        """
        :type S: str
        :rtype: List[str]
        """

        def permute(s, result):
            if not s: return result
            
            c = s[0]
            if c.isdigit():
                if not result:
                    result.append(c)
                else:
                    for i in range(len(result)):
                        result[i] += c
            elif c.isalpha():
                if not result:
                    result.append(c.upper())
                    result.append(c.lower())
                else:
                    r = []
                    for i in range(len(result)):
                        r.append(result[i] + c.upper())
                        r.append(result[i] + c.lower())
                    
                    result = r[:]
            return permute(s[1:], result)
        
        return permute(letters, [])
        
s = Solution()
print(s.letterCasePermutation("a1b2"))
        
