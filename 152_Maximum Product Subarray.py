class Solution(object):

    def maxProductDPSpace1(self, nums):
        '''永远记录最小值和最大值，乘以下一个数
        因为只看前一个状态(i-1) 所以不需要DP数组来保存，只需一个变量就好
        同理类似斐波那契数列如果需要看i-1和i-2，也只需要2个变量来保存前两个子问题的结果，不需要数组
        '''
        result = nums[0]
        
        dpmx = nums[0]
        dpmin = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                dpmx, dpmin = dpmin, dpmx
            
            dpmx = max(dpmx * nums[i], nums[i])
            dpmin = min(dpmin * nums[i], nums[i])
            
            result = max(dpmx, result)
        
        return result
    
    def maxProductDPSpaceN(self, nums):
        '''永远记录最小值和最大值，乘以下一个数'''
        """
        :type nums: List[int]
        :rtype: int
        """
        dpmax = [float('-inf')] * len(nums)
        dpmin = [float('inf')] * len(nums)
        
        dpmax[0] = nums[0]
        dpmin[0] = nums[0]
        
        for i in range(1, len(nums)):
            dpmax[i] = max(nums[i], nums[i] * dpmax[i - 1], nums[i] * dpmin[i - 1])
            dpmin[i] = min(nums[i], nums[i] * dpmax[i - 1], nums[i] * dpmin[i - 1])
        
        return max(dpmax)

    def maxProductPrefixSuffixProduct(selfself, nums):
        ''' 如果没有0，最大乘积子序列一定包括头或者尾 (正负数各种情况).求前缀乘积和后缀乘积取最大
                        如果有0，在0的地方重新开始一次子序列 以避免0的影响 
            3 4 0 -2 4 -> 乘积前缀 3 12 0 -2(1*-2) -8 
        '''
        a = nums
        b = nums[::-1]
        
        for i in range(1, len(nums)):
            a[i] *= a[i - 1] or 1
            b[i] *= b[i - 1] or 1

        return max(a + b)


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([1, 2, 0, 2, -3, 4, -9, 1]))
