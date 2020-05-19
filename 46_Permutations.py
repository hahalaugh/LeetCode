class Solution(object):

    def permute(self, nums):
        result = []
        for i in range(len(nums)):
            temp = nums[i]
            nums.pop(i)
            for j in range(len(nums)):
                nums.insert(j, temp)
                result.append(nums[:])
                nums.pop(j)
            nums.insert(i, temp)        
        return result
    
    def permuteBC(self, nums):
        # Backtracking
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def bc(r, nums):
            if not nums:
                result.append(r[:])
            else:
                for i in range(len(nums)):
                    r.append(nums[i])
                    temp = nums.pop(i)
                    bc(r, nums)
                    nums.insert(i, temp)
                    r.pop()

        bc([], nums)
        
        return result


s = Solution()
print(s.permute([1, 2, 3, 4 ]))
