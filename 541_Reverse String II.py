class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s: return s
        s = list(s)
        i = 0
        while i < len(s):
            l = i
            r = i+k-1 if i+k-1 < len(s) else len(s)-1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += k*2
        
        return "".join(s)
        
            
s = Solution()
print(s.reverseStr("abcdefg", 2))
print(s.reverseStr("abcdefg", 3))