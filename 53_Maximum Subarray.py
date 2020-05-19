class Solution(object):
    def maxSubArray(self, nums):
        #暴力，窗口，不过
        
        mx = float('-inf')
        
        for w in range(1, len(nums)+1):
            for i in range(len(nums)-w+1):
                mx = max(mx, sum(nums[i:i+w]))
        
        return mx
                
        
    def maxSubArrayDP(self, nums):
        #DP
        if not nums: return -1
        
        if len(nums) == 1: return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        
        return max(dp)
    
        
    def maxSubArrayMaxMin(self, nums):
        #记录当前和与当前最小值
        s = []
        m = []
        
        for n in nums:
            if not s: 
                s.append(n)
                m.append(0)
            else:
                s.append(s[-1] + n)
                m.append(min(s[-2], m[-1]))
        
        for i in range(len(s)):
            s[i] = s[i] - m[i]
        
        return max(s)
    
    def maxSubArrayTricky(self, nums):
        #HEDANE算法，DP的变种
        """
        :type nums: List[int]
        :rtype: int
        """
        #Tricky
        
        for i in range(1, len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        
        return max(nums)