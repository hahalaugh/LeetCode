class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #dabcabcff
        #dabc -> mx = 4
        #da(b)c[a] 新的序列应该从(b)处开始，所以新的下界i等于index(a)+1
        #之所以要更新i为i = max(d[s[j]]+1, i)是因为要防止i倒退, 例如abba.遇到第二个b的时候i已经指向第二个b,如果不采用最大值则遇到第二个a的时候i会回退到第一个b处,造成错误结果
        
        if not s: return 0
        
        d = {}
        mx = float('-inf')
        i = 0
        for j in range(len(s)):
            if s[j] in d:
                i = max(d[s[j]]+1, i)
            mx = max(mx, j - i + 1)
            d[s[j]] = j
        
        return mx
    
    def lengthOfLongestSubstringSlidingWindow(self, s):
        #Sliding Window
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        d = set()
        mx = float('-inf')
        i, j = 0, 0
        while j < len(s):
            while j < len(s) and s[j] not in d:
                d.add(s[j])
                mx = max(mx, len(d))
                j += 1
            
            if j == len(s):
                break
            
            d.remove(s[i])
            i += 1
        
        return mx
    