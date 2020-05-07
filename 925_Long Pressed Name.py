from __builtin__ import False
from pickle import FALSE


class Solution(object):

    def isLongPressedName(self, name, typed):
        #Group name 和 typed之后进行两两比较
        # ALEX -> (A,1),(L,1),(E,1),(X,1)
        # ALLEXX -> (A,1),(L,2),(E,1),(X,2)
        # 长度相同，每个位置上的字符匹配，typed 长度大于name。全部满足的就是True
        def group(s):
            r = []
            for i in range(len(s)):
                if r and s[i] == r[-1][0]:
                    t = r[-1]
                    r[-1] = (t[0], t[1] + 1)
                else:
                    r.append((s[i], 1))
            return r
        
        n = group(name)
        t = group(typed)
        if len(n) != len(t): return False
        
        for i in range(len(n)):
            if n[i][0] != t[i][0] or n[i][1] > t[i][1]:
                return False
    
        return True
        
        # return r
    
    def isLongPressedNameTwoPointer(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0  # name
        j = 0  # typed
        
        while i < len(name) and j < len(typed):
            print(name[i], typed[j])
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j < len(typed) - 1:
                    j = j + 1
                    if typed[j] != typed[j - 1] and typed[j] != name[i]:
                        return False
        
        return i == len(name)


s = Solution()
print(s.isLongPressedName("yyxbtsrs", "yyyyxbbtssrs"))
print(s.isLongPressedName("alex", "aaleexx"))
