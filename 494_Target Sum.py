class Solution(object):

    def findTargetSumWays(self, nums, s):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        d = {}
        
        def find(idx, goal):
            if (idx, goal) in d:
                return d[(idx, goal)]
            elif idx == 0:
                return int(goal == nums[idx]) + int(goal == -nums[idx])
            else:
                n = nums[idx]
                d[(idx, goal)] = find(idx - 1, goal + n) + find(idx - 1, goal - n)
                return d[(idx, goal)]
        
        return find(len(nums) - 1, s)


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(s.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
print(s.findTargetSumWays([40,2,49,50,46,6,5,23,38,45,45,17,4,26,40,33,14,9,37,24], 7))
