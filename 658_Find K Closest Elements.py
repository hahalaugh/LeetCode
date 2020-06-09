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
        i = 第一个大于等于x的元素位置
        j = 第一个大于x的元素位置
        1 2 [3i] 3 3 3 [4j] 5
        当x存在时，i一定大于j 1 2 [3i] [4j] 5 6
        当x不存在时，i一定等于j 1 2 [4 i j] 5 或 1 2 4 5 [i, j] 当 x = 6
        
        '''
        i, j = firstGreaterEqualTo(arr, x), firstGreaterTo(arr, x)

        '''r - 剩下还有几个要找'''
        r = k
        
        '''当x存在时，已经找到了j-i个'''
        if j > i: 
            r -= (j - i)
        
        '''当x存在时，使i和j都指向x元素, 1 2 [3i] 3 3 [3j] 5 6 或者 1 2 [3 i j] 4 5
        当x不存在时,把j移动到i前面。这是为了给之后的比较提供一致性  i-1 <-> j+1 
        1 2 3 4 5 [7ij] 7 8 -> 1 2 3 4 [5j] 7[i] 7 8
                如果先需要5的话就i-=1,如果先需要7的话就j+=1 
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
