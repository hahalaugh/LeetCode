class Solution(object):

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        def firstGreaterEqualTo(nums, x):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) / 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def firstGreaterTo(nums, x):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) / 2
                if nums[mid] <= x:
                    left = mid + 1
                else:
                    right = mid
            return left

        '''
        i = ��һ�����ڵ���x��Ԫ��λ��
        j = ��һ������x��Ԫ��λ��
        1 2 [3i] 3 3 3 [4j] 5
        ��x����ʱ��iһ������j 1 2 [3i] [4j] 5 6
        ��x������ʱ��iһ������j 1 2 [4 i j] 5 �� 1 2 4 5 [i, j] �� x = 6
        
        '''
        i, j = firstGreaterEqualTo(arr, x), firstGreaterTo(arr, x)

        '''r - ʣ�»��м���Ҫ��'''
        r = k
        
        '''��x����ʱ���Ѿ��ҵ���j-i��'''
        if j > i: 
            r -= (j - i)
        
        '''��x����ʱ��ʹi��j��ָ��xԪ��, 1 2 [3i] 3 3 [3j] 5 6 ���� 1 2 [3 i j] 4 5
        ��x������ʱ,��j�ƶ���iǰ�档����Ϊ�˸�֮��ıȽ��ṩһ����  i-1 <-> j+1 
        1 2 3 4 5 [7ij] 7 8 -> 1 2 3 4 [5j] 7[i] 7 8
                �������Ҫ5�Ļ���i-=1,�������Ҫ7�Ļ���j+=1 
        '''
        j -= 1
        
        if k <= 0:
            return arr[i] * k
        else:
            while r > 0:
                if i == 0: 
                    j += 1
                elif j == len(arr)-1:
                    i -= 1
                elif x - arr[i - 1] <= arr[j + 1] - x:
                    i -= 1
                else:
                    j += 1
                r -= 1
            return arr[i:j+1]

s = Solution()
print(s.findClosestElements([1], 1, 1))
print(s.findClosestElements([0, 1], 2, 1))
print(s.findClosestElements([0, 1], 2, 0))
print(s.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))
print(s.findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(s.findClosestElements([1, 1, 2, 3, 3, 3, 4, 6, 8, 8], 6, 1))
