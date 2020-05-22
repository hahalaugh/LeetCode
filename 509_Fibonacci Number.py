class Solution(object):

    def fib(self, n):
        # Recursive
        if n <= 1:
            return n
        
        p1 = 1
        p2 = 0
        fb = 0
        
        for i in range(n - 2 + 1):
            fb = p1 + p2
            p2 = p1
            p1 = fb
        return fb
        
    def fibTopDown(self, n):
        """
        :type N: int
        :rtype: int
        """
        d = {}

        def f(n):
            if n in d: return d[n]
            elif n <= 1: 
                return n
            else: 
                d[n] = f(n - 1) + f(n - 2)
                return d[n]
            
        return f(n)
    
    def fibBottomUp(self, n):
        if n <= 1: 
            return n
            
        a = [0, 1]
        
        for i in range(2, n + 1):
            a.append(a[-1] + a[-2])
            
        return a[n]
