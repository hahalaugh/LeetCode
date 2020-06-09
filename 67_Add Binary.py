class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a and not b: return None
        if not a or not b: return a or b
        
        r = []
        
        ia, ib = len(a)-1, len(b)-1
        c = 0
        
        while ia >= 0 and ib >= 0:
            v = int(a[ia]) + int(b[ib]) + c
            c = int(v > 1)
            v %= 2
            r.append(str(v))
            ia -= 1
            ib -= 1
        
        i = ia if ia >= 0 else ib
        a = a if ia >=0 else b
        
        while i >= 0:
            v = int(a[i]) + c
            c = int(v > 1)
            v %= 2
            r.append(str(v))
            i -= 1
        
        if c > 0:
            r.append(str(c))
        
        
        return "".join(r[::-1])
s = Solution()
print(s.addBinary("11", "1"))