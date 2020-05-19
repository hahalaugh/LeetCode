class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        
        result = []
        nums.sort()
        
        def bc(r, nums):
            if not nums:
                return result.append(r[:])
            else:
                for i in range(len(nums)):
                    #和前一个比较去除重复
                    if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                        r.append(nums[i])
                        temp = nums.pop(i)
                        bc(r, nums)
                        nums.insert(i, temp)
                        r.pop()

        bc([], nums)
        return result
