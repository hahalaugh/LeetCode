class Solution(object):

    def addDigits(self, num):
        return num % 9
    
    def addDigitsIteration(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        
        t = 0
        while True:
            while num > 0:
                t += num % 10
                num /= 10
            
            if t < 10:
                return t
            else:
                num = t
                t = 0


s = Solution()
r = []
for i in range(0, 100):
    r.append(s.addDigitsIteration(i))
print r
