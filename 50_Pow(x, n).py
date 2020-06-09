class Solution(object):
    def myPowBinary(self, x, n):
        if n < 0:
            n = abs(n)
            x = 1 / float(x)
         
        def pow(x, n):
            if n == 0: 
                return 1
            
            if n % 2 == 0:
                return pow(x, n / 2) ** 2
            else:
                return pow(x, (n - 1) / 2) ** 2 * x
        
        return pow(x, n)

    def myPowRecursive(self, x, n):
        if n < 0:
            n = abs(n)
            x = 1 / float(x)
        
        def pow(x, n):
            if n == 0: return 1
            return x * pow(x, n - 1)
        
        return pow(x, n)
    
    def myPowIterate(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        
        if n < 0:
            n = abs(n)
            x = 1 / float(x)
        
        t = 1
        for i in range(n):
            print(i)
            t *= x
        
        return t


s = Solution()
# print(s.myPowRecursive(1.00001, 13))
# print(s.myPowIterate(1.00001, 123456))
print(s.myPowBinary(1.00001, 2 ** (23) - 1))
