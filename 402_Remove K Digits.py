class Solution(object):

    def removeKdigits(self, num, k):
        if not num: return '0'
        s = []
        for n in num:
            while k and s and s[-1] > n:
                """IF new character is smaller"""
                s.pop()
                k -= 1
            s.append(n)

        while s and s[0] == '0':
            s.pop(0)
            k -= 1
        
        while s and k > 0:
            s.pop()
            k -= 1
        
        return ''.join(s) if s else '0'
        
        
s = Solution()
print(s.removeKdigits("1432219", 3))
print(s.removeKdigits("10200", 1))
