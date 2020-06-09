class Solution(object):
    def isPowerOfThree(self, n):
        #先生成3的幂的数组
        if n == 0: return False
        s = set()
        t = 1
        while t <= 2**(32-1):
            s.add(t)
            t *= 3
        return n in s
        
    def isPowerOfThreeDivision(self, n):
        #一直除以三看余数
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        
        while n >= 3:
            n /= float(3)
        
        return n == float(1)
    