class Solution(object):
    def isHappy(self, n):
        #O(1) space
        def next(n):
            t = 0
            while n > 0:
                t += (n % 10)**2
                n /= 10
            return t

        slow, fast = n, n
        while True:
            slow = next(slow)
            fast = next(fast)
            fast = next(fast)
            if slow == fast:
                return slow == 1
        
    def isHappyON(self, n):
        #O(N) space
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n > 1:
            if n in s: return False
            s.add(n)
            t = 0
            while n > 0:
                t += (n % 10)**2
                n /= 10
            n = t
        return True