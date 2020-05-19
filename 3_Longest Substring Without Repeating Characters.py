class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #dabcabcff
        #dabc -> mx = 4
        #da(b)c[a] �µ�����Ӧ�ô�(b)����ʼ�������µ��½�i����index(a)+1
        #֮����Ҫ����iΪi = max(d[s[j]]+1, i)����ΪҪ��ֹi����, ����abba.�����ڶ���b��ʱ��i�Ѿ�ָ��ڶ���b,������������ֵ�������ڶ���a��ʱ��i����˵���һ��b��,��ɴ�����
        
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
    