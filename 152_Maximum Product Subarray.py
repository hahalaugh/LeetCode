class Solution(object):

    def maxProductDPSpace1(self, nums):
        '''��Զ��¼��Сֵ�����ֵ��������һ����
        ��Ϊֻ��ǰһ��״̬(i-1) ���Բ���ҪDP���������棬ֻ��һ�������ͺ�
        ͬ������쳲��������������Ҫ��i-1��i-2��Ҳֻ��Ҫ2������������ǰ����������Ľ��������Ҫ����
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
        '''��Զ��¼��Сֵ�����ֵ��������һ����'''
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
        ''' ���û��0�����˻�������һ������ͷ����β (�������������).��ǰ׺�˻��ͺ�׺�˻�ȡ���
                        �����0����0�ĵط����¿�ʼһ�������� �Ա���0��Ӱ�� 
            3 4 0 -2 4 -> �˻�ǰ׺ 3 12 0 -2(1*-2) -8 
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
