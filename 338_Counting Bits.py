class Solution(object):
    def countBits(self, num):
        """
        DP f(4-7) = f(0-3) + 1
           f(8-15) = f(0-7) + 1 
        """
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0: return [0]
        if num == 1: return [0, 1]
        
        dp = [0] * (num+1)
        dp[1] = 1
        
        t = 1
        while True:
            n = 0
            for i in range (2**t, 2**(t+1)):
                dp[i] = dp[n] + 1
                n += 1
                if i == num:
                    return dp
            
            t += 1